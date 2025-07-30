"""Module containing Dancing Links and associated classes and functions."""


class RowHeader(object):
    """Special header; links to the first ColumnHeader."""
    def __init__(self):
        self.right = None

    def add_right(self, node):
        self.right = node
        node.left = self


class ColumnHeader(object):
    """Column header; contains links to adjacent column headers, and the first
    DLX in the column."""
    def __init__(self, constraint):
        self.constraint = constraint
        self.left = self.right = self.down = None
        self.count = 0

    def get_count(self):
        """Number of DLX nodes under the column header."""
        return self.count

    def append(self, dlx):
        """Add DLX node to bottom of column."""
        self.count += 1
        node = self
        while node.down:
            node = node.down
        node.down = dlx
        dlx.up = node

    def add_right(self, node):
        """Add ColumnHeader to right of current node."""
        self.right = node
        node.left = self

    def delete(self, deleted_nodes):
        """Delete-from-row every node in the column."""
        self.delete_from_column()
        node = self.down
        while node:
            node.delete_row(deleted_nodes=deleted_nodes)
            node = node.down

    def delete_from_column(self):
        """Delete header from column headers."""
        if self.left : self.left.right = self.right
        if self.right : self.right.left = self.left

    def undelete_from_column(self):
        """Re-add header to column headers."""
        if self.left : self.left.right = self
        if self.right : self.right.left = self


class DLX(object):
    """Linked list containing references to adjacent nodes
    above & below, and left & right, as well as a singly-linked reference to 
    the column header.
    """
    def __init__(self, header, row_id):
        self.row_id = row_id
        self.header = header
        self.up = self.down = self.left = self.right = None

    def delete_row(self, delete_columns=False, deleted_nodes=None):
        """Delete all nodes in current row.
        Arguments:
            bool delete_columns: If True, delete_row will delete all column
                headers in the row, and any rows within those columns.
                Otherwise, delete_row just deletes the current row.
            list<DLX> deleted_nodes: List of all nodes deleted by delete_row.
        Returns:
            list<DLX>: The mutated deleted_nodes list. Used to undelete the nodes.
                TODO: can this list be efficiently inferred instead?
        """
        node = self
        while node.left:
            node = node.left
        while node:
            if delete_columns:
                node.header.delete(deleted_nodes)
            else:
                node.delete_from_row()
                deleted_nodes.append(node)
            node = node.right
        return deleted_nodes

    def undelete_row(self, deleted_nodes=None):
        """Undelete deleted_nodes in reverse order, then undelete column headers."""
        for i in range(len(deleted_nodes)-1,-1,-1):
            deleted_nodes[i].undelete_from_row()
        node = self
        while node.right:
            node = node.right
        while node:
            node.header.undelete_from_column()
            node = node.left

    def delete_from_row(self):
        if self.up : self.up.down = self.down
        if self.down : self.down.up = self.up
        self.header.count -= 1

    def undelete_from_row(self):
        if self.up : self.up.down = self
        if self.down : self.down.up = self
        self.header.count += 1

    def __str__(self):
        return str((self.row_id, self.header.constraint))


def get_column_header(row_header, constraint):
    """Given the row header and a constraint, return the matching column
    header."""
    node = row_header.right
    while node:
        if node.constraint == constraint:
            return node
        node = node.right
    return None


def build_dlx(constraints, elements, mapping):
    """
    Arguments:
        list<T> constraints: constraints to be satisfied.
        list<list<T>> elements: such that each element satisfies one or more
            constraints.
        lambda<list<T>:list<T>> mapping: such that mapping(element) = a sublist
            of satisfied constraints.
    Returns:
        RowHeader: a row header linked to the first column header
            (such that the column headers are linked to DLX representing a
            mapping of elements to constraints)
    """
    row_header = RowHeader()
    prev_node = row_header
    for constraint in constraints:
        column_header = ColumnHeader(constraint)
        prev_node.add_right(column_header)
        prev_node = column_header

    for element in elements:
        matched_constraints = mapping(element)
        prev_row = None
        for constraint in matched_constraints:
            header = get_column_header(row_header, constraint)
            new_node = DLX(header, element)
            header.append(new_node)
            if prev_row:
                prev_row.right = new_node
                new_node.left = prev_row
            prev_row = new_node

    return row_header


def all_exact_covers(constraints, elements, mapping):
    """Find all exact covers for a given constraints, elements and mapping.
    Arguments:
        list<T> constraints: constraints to be satisfied.
        list<list<T>> elements: such that each element satisfies one or more
            constraints.
        lambda<list<T>:list<T>> mapping: such that mapping(element) = a sublist
            of satisfied constraints.
    Returns:
        list<list<list<T>>>: list of all sublists of elements, such that each
            sublist is an exact cover of the constraints.
    """
    row_header = build_dlx(constraints, elements, mapping)
    exact_covers = []
    _all_exact_covers(row_header, [], exact_covers)
    return exact_covers


def _all_exact_covers(row_header, partial_solution, full_solutions):
    """Helper for all_exact_covers. Keeps track of current partial and full covers."""
    node = row_header.right
    if not node:
        # Partial solution satisfies all constraints.
        full_solutions.append([x for x in partial_solution])
        return
    column = None
    while node:
        # Find constraint with fewest matching elements.
        node_count = node.get_count()
        if node_count <= 0:
            # A constraint is un-satisfiable given current partial solution.
            return
        if not column or node_count < column.get_count():
            column = node
        node = node.right
    dlx = column.down
    while dlx:
        # Find all solutions featuring each element in column.
        partial_solution.append(dlx.row_id)
        deleted_nodes = []
        deleted_nodes = dlx.delete_row(
            delete_columns=True, deleted_nodes=deleted_nodes)
        _all_exact_covers(row_header, partial_solution, full_solutions)
        dlx.undelete_row(deleted_nodes=deleted_nodes)
        partial_solution.remove(dlx.row_id)
        dlx = dlx.down
