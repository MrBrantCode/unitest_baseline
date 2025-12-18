"""
QUESTION:
Write a function `word_frequency` that takes a string `input_string` as input and returns a dictionary containing the frequency of each word in the string. The function should ignore any non-alphanumeric characters and consider words in a case-insensitive manner. The input string contains words separated by spaces and has a length between 1 and 10^5.
"""

import string
from collections import defaultdict

def word_frequency(input_string: str) -> dict:
    strip = string.whitespace + string.punctuation + string.digits + "\"'"
    input_string = ''.join(char if char not in strip else ' ' for char in input_string)
    words = defaultdict(int)
    for word in input_string.lower().split():
        words[word] += 1
    return dict(words)