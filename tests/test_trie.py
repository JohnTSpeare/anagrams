"""Test module for Trie."""
import unittest

from anagrams.trie import Trie


class Test_Trie(unittest.TestCase):
    """Test class for Trie."""
    def setUp(self):
        self.trie = Trie()
        self.trie.add("test1")
        self.trie.add("test2")

    def test_add(self):
        """Test for add."""
        self.assertFalse(self.trie.contains("test3"))
        self.trie.add("test3")
        self.assertTrue(self.trie.contains("test3"))

    def test_remove(self):
        """Test for remove."""
        self.assertTrue(self.trie.contains("test1"))
        self.trie.remove("test1")
        self.assertFalse(self.trie.contains("test1"))

    
