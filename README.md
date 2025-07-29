# anagrams
CLI tool for finding anagrams of a given word or phrase.

List of dictionary words was taken from:
https://websites.umich.edu/~jlawler/wordlist


## Usage

> python anagrams "A word or phrase"


## Running Unit Tests

It is assumed docker is installed and running.
Unit tests are run via pytest, within a docker container with the relevant
packages installed. Unit tests can be run via the following command (from the
project's root directory):

```
> make test
```
