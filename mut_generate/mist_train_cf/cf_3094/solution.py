"""
QUESTION:
Implement a function called `count_word_occurrences` that takes a string as input and returns a dictionary where the keys are the unique words and the values are their corresponding counts. The function should preserve the order of occurrence of unique words and handle punctuation marks and special characters as separators between words. Do not use any built-in functions or libraries for this task, except for the `re` module for regular expressions.
"""

import re

def count_word_occurrences(string):
    word_counts = {}
    words = re.split(r'\W+', string)
    for word in words:
        if word:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    return word_counts