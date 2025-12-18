"""
QUESTION:
Create a function named `get_first_last_words` that takes an array of strings as input and returns an array of tuples. Each tuple contains the first and last word of each string, ignoring leading/trailing whitespace and punctuation marks. The function should handle empty input, strings with one word, multiple consecutive spaces, and punctuation marks. The function should return an empty array if the input array is empty. The time complexity of the function should be O(n), where n is the total number of characters in the input array.
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
            tuples.append((words[0], words[-1]))
    return tuples