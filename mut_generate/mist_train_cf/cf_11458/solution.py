"""
QUESTION:
Write a function `calculate_word_lengths` that takes a string as input, calculates the length of each word, and returns a list of word lengths in descending order. If two words have the same length, sort them alphabetically, and if they have the same length and alphabetical order, maintain their original order. The input string may contain punctuation marks and numbers, which should be ignored when calculating word lengths.
"""

def calculate_word_lengths(string):
    clean_string = ''.join(e for e in string if e.isalpha() or e.isspace())
    words = clean_string.split()
    word_lengths = [(len(word), word) for word in words]
    word_lengths.sort(key=lambda x: (-x[0], x[1]))
    return [x[0] for x in word_lengths]