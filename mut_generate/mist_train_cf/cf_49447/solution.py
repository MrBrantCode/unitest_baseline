"""
QUESTION:
Create a function `words_string` that takes two parameters: a string `s` containing words separated by commas, spaces, or a combination of both, and a target word. The function should split the string into words, remove all occurrences of the target word, and return a list of the remaining words in reverse order with each word reversed.
"""

import re

def words_string(s, target):
    words_list = re.findall(r"[\w']+", s.replace(',', ' '))
    result = [word[::-1] for word in words_list if word != target]
    return result