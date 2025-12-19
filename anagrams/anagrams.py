"""Module for determining anagrams of a given word or phrase."""
import re

from dlx import all_exact_covers
from words.dictionary import get_valid_jumbles, get_valid_words


def get_anagrams(word):
    """Get anagrams of given word."""
    print("Finding anagrams for: %r" % word)
    letters = re.sub(r"[^a-z]+", "", word.lower())
    print("Given letters: %r" % letters)
    numbers = [i for i in range(len(letters))]
    key = lambda nums: "".join([letters[i] for i in nums])
    print("Determining words that can be made from these letters... ...")
    word_list = get_valid_words(letters)
    print("Done.")
    print("Words found:")
    print(", ".join([jumble for jumble in word_list]))

    # TODO: add ability to filter words out of word_list.
    # TODO: add ability to require certain words to appear in the final
    # anagrams (NOTE: this will require updates to dlx.py).

    number_list = words_to_nums(word_list, letters)

    print("\nAnagrams:")
    constraints = numbers
    elements = number_list
    mapping = lambda element: element
    coded_anagrams = all_exact_covers(constraints, elements, mapping)
    anagrams = []
    for coded_anagram in coded_anagrams:
        anagram = [key(coded_word) for coded_word in coded_anagram]
        print(", ".join(anagram))
        anagrams.append(anagram)
    return anagrams


def words_to_nums(word_list, letters):
    """Converts list of words to list of list of numbers mapping to index
    values of user's original word-or-phrase, taking duplicate letters into
    account.
    """
    number_list = []
    char_list = {}
    for i in range(len(letters)):
        char = letters[i]
        char_list.setdefault(char, [])
        char_list[char].append(i)
    for word in word_list:
        number_list += word_to_nums(word, char_list)

    return number_list


def word_to_nums(word, char_list):
    nums = []
    number_lists = []
    for char in word:
        number_lists.append(char_list[char])

    nums = _expand_number_list(number_lists)

    return nums


def _expand_number_list(number_lists):
    if not number_lists:
        return []
    elif len(number_lists) == 1:
        return [[num] for num in number_lists[0]]
    expanded_number_list = []
    expanded_sub_list = _expand_number_list(number_lists[1:])
    for num in number_lists[0]:
        for l in expanded_sub_list:
            if not num in l:
                expanded_number_list.append([num] + l)
    return expanded_number_list
