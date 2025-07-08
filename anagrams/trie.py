"""Module containing Trie class."""


class Trie(object):
    """Stores a list of lists in a Trie tree structure."""
    def __init__(self):
        self.children = {}
        self.terminal = False

    def add(self, item):
        """Add a list to the trie."""
        if len(item) <= 0:
            self.terminal = True
            return
        if item[0] not in self.children:
            self.children[item[0]] = Trie()
        self.children[item[0]].add(item[1:])

    def remove(self, item):
        """Remove a list from the trie."""
        if len(item) <= 0:
            self.terminal = False
            return
        if item[0] in self.children:
            self.children[item[0]].remove(item[1:])
        
    def contains(self, item):
        """Returns true iff trie contains item."""
        if len(item) <= 0:
            return self.terminal
        if not item[0] in self.children:
            return False
        return self.children[item[0]].contains(item[1:])
