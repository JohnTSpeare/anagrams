"""Test module for anagrams."""
import unittest

import mock

from anagrams.anagrams import get_anagrams

class Test_Anagrams(unittest.TestCase):
    """Test class for get_anagrams."""
    def setUp(self):
        self.test_word = "test 1!"
        self.expected_letters = "test"
        self.expected_numbers = [0, 1, 2, 3]

    @mock.patch("anagrams.anagrams.get_valid_words")
    @mock.patch("anagrams.anagrams.all_exact_covers")
    def test_get_anagrams(self, mock_all_exact_covers, mock_get_valid_words):
        """Test for get_anagrams."""
        mock_get_valid_words.return_value = ["te", "st"]
        mock_all_exact_covers.return_value = [
            [[0, 1], [2, 3]],
        ]

        anagrams = get_anagrams(self.test_word)
        
        mock_get_valid_words.assert_called_once_with("test")

        # TODO: This is messy. Figure out a way to mock the lambdas
        self.assertEqual(len(mock_all_exact_covers.call_args_list), 1)
        self.assertEqual(
            mock_all_exact_covers.call_args_list[0][0][0:2],
            ([0, 1, 2, 3], [[0, 1], [3, 1], [2, 0], [2, 3]]),
        )

        self.assertEqual(anagrams, [["te", "st"]])
