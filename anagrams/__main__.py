"""Main module for anagram."""
import argparse

from anagrams import get_anagrams


def setup_arguments():
    parser = argparse.ArgumentParser(
        prog="Anagrams",
        description="Find anagrams for a given a word or phrase.",
    )
    parser.add_argument(
        "word",
        help="Word or phrase.",
    )
    args = parser.parse_args()
    return args


def main():
    args = setup_arguments()
    get_anagrams(args.word)
    return 0


if __name__ == "__main__":
    main()
