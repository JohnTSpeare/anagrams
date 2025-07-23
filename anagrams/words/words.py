"""Module containing functions / classes related to finding valid dictionary words."""


class Dictionary(object):
    """Keeps track of valid dictionary words."""
    def __init__(self):
        with open("word_list.txt", "r") as f:
            self.words = f.read().split("\n")

    def is_valid(self, word):
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
    """Find all combinations of letters in a word."""
    jumbled_words = []
    for letter in word:
        jumbled_words += _add_letter_to_words(letter, jumbled_words)
        jumbled_words.append(letter)
    return jumbled_words


def _add_letter_to_words(letter, words):
    """Helper for jumble."""
    added_words = []
    for word in words:
        for i in range(len(word)+1):
            added_words.append(word[0:i] + letter + word[i:])
    return added_words
