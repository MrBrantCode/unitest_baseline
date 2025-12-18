"""
QUESTION:
Create a function `separate_and_count_words` that takes an input string and a set of excluded words as parameters, and returns a dictionary containing the count of each unique word in the string, excluding common words, numbers, special characters, and the provided excluded words. The function should handle hyphenated words as separate words and be case-insensitive.
"""

import re
from collections import Counter

def separate_and_count_words(input_string, excluded_words=None):
    input_string = input_string.lower()
    word_pattern = re.compile(r'\b\w+\b')
    words = word_pattern.findall(input_string)
    word_counter = Counter()

    if not excluded_words:
        excluded_words = set(['the', 'a', 'is', 'and', 'of', 'in'])

    for word in words:
        if re.match(r'^[a-zA-Z\-]+$', word):
            if word not in excluded_words:
                word_counter[word] += 1

    return word_counter