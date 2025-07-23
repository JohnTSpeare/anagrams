"""Wrapper module; determines anagrams of a given word or phrase."""
import re

from dlx import all_exact_covers
from words.dictionary import get_valid_jumbles


def get_anagrams(word):
    letters = re.sub(r"[\W0-9_]+", "", word.lower())
    numbers = [i for i in range(len(letters))]
    key = lambda nums: "".join([letters[i] for i in nums])
    jumbles = get_valid_jumbles(numbers, key=key)
    # jumbles = get_valid_jumbles(letters, key=None)
    print(word)
    print(letters)
    print(numbers)
    print(jumbles)  # buncha nums
    print(", ".join(["".join(key(jumble)) for jumble in jumbles]))  # equivalent words

    print("Anagrams:")
    constraints = numbers
    elements = jumbles
    mapping = lambda element: [x for x in constraints if x in element]
    anagrams = all_exact_covers(constraints, elements, mapping)
    for anagram in anagrams:
        print(", ".join([key(coded_word) for coded_word in anagram]))
