"""
QUESTION:
Implement a function `validate_isbn_10(isbn)` to validate an International Standard Book Number (ISBN-10). The function should take a string `isbn` as input, remove any hyphens, and return `True` if the input is a valid ISBN-10 and `False` otherwise. A valid ISBN-10 should have a length of 10, numeric characters in the first 9 positions, and either a digit or 'X' in the last position.
"""

import string

def validate_isbn_10(isbn: str) -> bool:
    isbn = isbn.replace('-', '')
    if len(isbn) != 10 or not isbn[:-1].isnumeric() or isbn[-1] not in string.digits + 'X':
        return False
    return True