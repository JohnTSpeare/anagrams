"""Module containing functions / classes related to finding valid dictionary words."""
import os


class Dictionary(object):
    """Keeps track of valid dictionary words."""
    def __init__(self):
        self.words = self._get_word_list()

    def _get_word_list(self):
        word_list = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "word_list.txt",
        )
        with open(word_list, "r") as f:
            return f.read().rstrip().split("\n")

    def valid_word(self, word):
        """Return True iff word is in the dictionary."""
        return bin_search(word, self.words)


def bin_search(item, sorted_list, start=None, end=None):
    """Binary search on sorted list."""
    if start is None:
        start = 0
        end = len(sorted_list)
    if end <= start:
        return False
    mid = start + int((end-start) / 2)
    if item == sorted_list[mid]:
        return True
    elif item < sorted_list[mid]:
        return bin_search(item, sorted_list, start=start, end=mid)
    else:
        return bin_search(item, sorted_list, start=mid+1, end=end)


def jumble(word):
    """Find all combinations of letters in a word.
    Arguments:
        list<T> word: typically a string, but can also be a coded number list.
    Returns:
        list<list<T>> jumbled words.
    """
    jumbled_words = []
    for letter in word:
        jumbled_words += _add_letter_to_words(letter, jumbled_words)
        jumbled_words.append([letter])
    return jumbled_words


def _add_letter_to_words(letter, words):
    """Helper for jumble."""
    added_words = []
    for word in words:
        for i in range(len(word)+1):
            added_words.append(word[0:i] + [letter] + word[i:])
    return added_words


def get_valid_jumbles(word, key=None, dictionary=None):
    """Given a word, find all word jumbles that appear in a Dictionary.
    Arguments:
        list<T> word: typically a string, but can be a coded number list.
        lambda<list<T>:str> key: key for translating a non-string
            jumbled word into a string, to be checked against the Dictionary.
            Defaults to converting character list to string.
    """
    if not key:
        key = lambda x: "".join(x)
    if not dictionary:
        dictionary = Dictionary()
    jumbles = jumble(word)
    return [jumble for jumble in jumbles \
        if dictionary.valid_word(key(jumble))]


def get_valid_words(word, dictionary=None):
    if not dictionary:
        dictionary = Dictionary()
    valid_words = []
    word_len = len(word)
    char_count = {}
    for char in word:
        char_count.setdefault(char, 0)
        char_count[char] += 1

    for valid_word in dictionary.words:
        if len(valid_word) > word_len:
            continue
        invalid_char = False
        valid_word_char_count = {}
        for char in valid_word:
            valid_word_char_count.setdefault(char, 0)
            valid_word_char_count[char] += 1
            if (not char in char_count or \
                    valid_word_char_count[char] > char_count[char]):
                invalid_char = True
                break
        if not invalid_char:
            valid_words.append(valid_word)

    return valid_words
