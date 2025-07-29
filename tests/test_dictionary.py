"""Test module for Dictionary."""
import mock
import pytest

import anagrams.words.dictionary as dictionary


class Test_Dictionary(object):
    """Test module for dictionary."""
    @pytest.fixture(autouse=True)
    @mock.patch("anagrams.words.dictionary.Dictionary._get_word_list")
    def setUp(self, mock_get_word_list):
        self.words = ["word1", "word2", "word3"]
        mock_get_word_list.return_value = self.words
        self.dictionary = dictionary.Dictionary()

    @pytest.mark.parametrize(
        "word,valid_word",
        [
            ("word1", True),
            ("word2", True),
            ("word3", True),
            ("word4", False),
        ]
    )
    def test_valid_word(self, word, valid_word):
        """Test for valid_word."""
        assert self.dictionary.valid_word(word) == valid_word


class Test_Jumbles(object):
    """Test module for jumble and get_valid_jumbles."""
    def test_jumble(self):
        """Test for jumble."""
        assert dictionary.jumble("ab") == [['a'], ['b', 'a'], ['a', 'b'], ['b']]

    @mock.patch("anagrams.words.dictionary.jumble")
    @mock.patch("anagrams.words.dictionary.Dictionary")
    def test_get_valid_jumbles(self, mock_dictionary, mock_jumble):
        """Test for get_valid_jumbles."""
        mock_jumble.return_value = [
            [char for char in "word1"],
            [char for char in "word2"],
        ]
        mock_dictionary.valid_word.side_effect = [False, True]
        result = dictionary.get_valid_jumbles("test", dictionary=mock_dictionary)
        mock_jumble.assert_called_once_with("test")
        assert result == [[char for char in "word2"]]
