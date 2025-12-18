"""
QUESTION:
Define a function `count_words(string)` that takes a string as input and returns the number of words in the string. A word is defined as a sequence of alphabetic characters separated by at least one space, punctuation mark, or digit. The function should be case sensitive and able to handle strings containing special characters. Use regular expressions to solve the problem.
"""

import re

def count_words(string):
    pattern = r'\b[a-zA-Z]+\b'
    word_list = re.findall(pattern, string)
    return len(word_list)