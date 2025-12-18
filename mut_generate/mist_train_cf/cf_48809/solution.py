"""
QUESTION:
Write a function `find_hello(text)` that uses a regular expression pattern to match any sequence of characters in a string that includes the term "hello". The function should be case insensitive and return all matches in the form of a list.
"""

import re

def find_hello(text):
    pattern = re.compile('.*hello.*', re.I)
    result = pattern.findall(text)
    return result