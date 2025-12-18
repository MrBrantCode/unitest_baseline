"""
QUESTION:
Create a function called `get_first_last_words` that takes an array of strings as input. The function should return an array of tuples, where each tuple contains the first and last word of the corresponding input string. The function should ignore leading and trailing whitespace in each string, handle consecutive spaces, and remove punctuation marks from words. The function should return an empty array if the input array is empty.
"""

import re

def get_first_last_words(strings):
    if not strings:
        return []

    tuples = []
    for string in strings:
        string = string.strip()
        string = re.sub(r'[^\w\s]', '', string)
        words = string.split()

        if len(words) >= 2:
            first_word = words[0]
            last_word = words[-1]
            tuples.append((first_word, last_word))

    return tuples