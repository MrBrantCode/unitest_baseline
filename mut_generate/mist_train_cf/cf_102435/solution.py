"""
QUESTION:
Write a function `count_words` that takes a string as input and returns a dictionary with the count of each word in the string. The string may contain spaces, punctuation marks, special characters, and numbers, but only words with at least 3 characters should be considered. The function should be case-sensitive and able to handle strings up to 1 million characters in length.
"""

import re

def count_words(string):
    string = re.sub(r'[^\w\s]', '', string)
    words = string.split()
    word_count = {}
    for word in words:
        if len(word) >= 3:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count