"""
QUESTION:
Write a function `pattern_check(input_string)` that returns `True` if the string contains the word "hello" followed by the word "world" anywhere in the string, and `False` otherwise. The words "hello" and "world" must be whole words, not part of other words.
"""

import re

def pattern_check(input_string):
    pattern = r'\bhello\b.*\bworld\b'
    return bool(re.search(pattern, input_string))