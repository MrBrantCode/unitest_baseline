"""
QUESTION:
Create a function called `test_isbn` that takes an ISBN string as input and returns `True` if the ISBN string matches the correct format of either a 10-digit or 13-digit International Standard Book Number (ISBN), and `False` otherwise. The function should match ISBNs that start with either '978' or '979' for 13-digit format or do not have a prefix for 10-digit format. The last character of the ISBN can be either a digit or 'X'.
"""

import re

def test_isbn(isbn):
    pattern = r"^(97(8|9))?\d{9}(?:\d|X)$"
    result = re.match(pattern, isbn)
    return result is not None