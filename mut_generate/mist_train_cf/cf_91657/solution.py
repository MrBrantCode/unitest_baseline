"""
QUESTION:
Create a function called `word_count` that takes a string as input and returns a dictionary where the keys are the unique words in the string and the values are their respective occurrence counts. The function should ignore punctuation and be case-insensitive.
"""

import re

def word_count(s):
    string = re.sub(r'[^\w\s]', '', s).lower()
    words = string.split()
    word_count_dict = {}
    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict