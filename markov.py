"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(input_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    whole_text = ""
    with open(input_path) as file:
        open_file = file.read()

#    open_file = open(input_path)

    return open_file


def make_chains(open_file):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    # your code goes here

    words = open_file.split()
    for idx in range(len(words) - 2):

        key = (words[idx], words[idx + 1])
        if key in chains:
            chains[key].append(words[idx + 2])
        else:
            chains[key] = [words[idx + 2]]

    return chains


def make_text(chains):
    """Return text from chains."""
    words = []
    key = choice(chains.keys())
    words.extend(key)

    while key in chains:
        new_val = choice(chains[key])
        key = (key[1], new_val)
        words.append(new_val)

    # your code goes here

    print " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)
