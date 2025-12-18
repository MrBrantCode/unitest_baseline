"""
QUESTION:
Write a function `d(test)` that uses the `re` module's `match` method to find all digit characters in the `test` input. The function should return a string of all digit characters found in the `test` input. Note that the `re` module's `match` method can only find the first occurrence of the pattern, so it is expected that the function will not directly use `re.match` but instead use an alternative method from the `re` module that can find all occurrences of the pattern.
"""

import re

def d(test):
    digits = re.findall(r'\d', test)
    return ''.join(digits)