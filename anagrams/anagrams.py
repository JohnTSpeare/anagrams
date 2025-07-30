"""Module for determining anagrams of a given word or phrase."""
import re

from dlx import all_exact_covers
from words.dictionary import get_valid_jumbles


def get_anagrams(word):
    """Get anagrams of given word."""
    print("Finding anagrams for: %r" % word)
    letters = re.sub(r"[^a-z]+", "", word.lower())
    print("Given letters: %r" % letters)
    numbers = [i for i in range(len(letters))]
    key = lambda nums: "".join([letters[i] for i in nums])
    print("Determining words that can be made from these letters... ...")
    jumbles = get_valid_jumbles(numbers, key=key)
    print("Done.")
    word_list = set()
    for jumble in jumbles:
        word_list.add(key(jumble))
    print("Words found:")
    print(", ".join([jumble for jumble in word_list]))

    # TODO: add ability to filter words out of word_list.

    print("\nAnagrams:")
    constraints = numbers
    elements = jumbles
    mapping = lambda element: element
    coded_anagrams = all_exact_covers(constraints, elements, mapping)
    anagrams = []
    for coded_anagram in coded_anagrams:
        anagram = [key(coded_word) for coded_word in coded_anagram]
        print(", ".join(anagram))
        anagrams.append(anagram)
    return anagrams
