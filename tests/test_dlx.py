"""Test module for DLX."""
import unittest

import anagrams.dlx as dlx


class Test_AllExactCovers(unittest.TestCase):
    """Test class for all_exact_covers."""
    def setUp(self):
        self.constraints = [0,1,2,3,4]
        self.elements = [
            [1,3,4],
            [0,1],
            [2],
            [3,4],
            [1,2,3,4],
            [0],
            [0,1,2,3],
        ]
        self.mapping = lambda element: element

    def test_all_exact_covers(self):
        result = dlx.all_exact_covers(
            self.constraints, self.elements, self.mapping)
        self.assertEqual(
            result,
            [
                [[0, 1], [2], [3, 4]],
                [[0], [1, 3, 4], [2]],
                [[0], [1, 2, 3, 4]],
            ]
        )
