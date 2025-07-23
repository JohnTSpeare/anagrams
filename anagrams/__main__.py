"""Main module for anagram."""
import argparse
import sys


def setup_arguments():
    parser = argparse.ArgumentParser(
        prog="Anagrams",
        description="Find anagrams given a word or phrase.",
    )
    parser.add_argument(
        "word",
        help="Word or phrase.",
    )
    args = parser.parse_args()
    return args


def main():
    args = setup_arguments()
    # TODO
    return 0


if __name__ == "__main__":
    main()
