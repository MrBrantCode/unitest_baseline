"""
QUESTION:
Create a function `count_words` that takes a string as input and returns a dictionary where the keys are the unique words in the string (in lowercase) and the values are their corresponding counts. The function should ignore punctuation marks and special characters, and consider numbers as separate words.
"""

import re
from collections import defaultdict

def count_words(string):
    # Convert the string to lowercase and split into words
    words = re.findall(r'\w+', string.lower())

    # Count the occurrences of each word using a defaultdict
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1

    # Convert the defaultdict to a regular dictionary
    word_count = dict(word_count)

    return word_count