"""
QUESTION:
Write a function `check_hello_world(text)` that takes a string `text` as input and returns `True` if the string contains the words "hello" and "world" separated by no more than three words, and `False` otherwise. The words in between "hello" and "world" should not contain any punctuation marks. The function should use a regular expression to match the pattern.
"""

import re

def check_hello_world(text):
    pattern = r"hello(\s+\b\w+\b){0,3}\s+world"
    return bool(re.search(pattern, text))