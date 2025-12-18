"""
QUESTION:
Write a function `word_frequency_counter` that takes a string `input_string` as input and returns a dictionary where the keys are the unique words in the input string and the values are the frequencies of each word. The function should be case-insensitive and treat non-alphanumeric characters as delimiters between words. The function should also handle edge cases such as empty input strings and strings with no alphanumeric characters.
"""

import re

def word_frequency_counter(input_string: str) -> dict:
    word_freq = {}
    words = re.findall(r'\b\w+\b', input_string.lower())
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq