"""
QUESTION:
Create a function called `extract_book_info` that takes a list of strings representing book editions in the format "Edition - Month/Year - ISBN" and returns a dictionary where the keys are the edition numbers and the values are the corresponding ISBN numbers. The edition number is always at the beginning of the string, followed by a hyphen and a space, and the ISBN is always at the end of the string after the last occurrence of "ISBN".
"""

import re

def extract_book_info(editions):
    book_info = {}
    for edition in editions:
        match = re.search(r'^(.*?) - .*? - (ISBN .*)$', edition)
        if match:
            edition_number = match.group(1)
            isbn = match.group(2)
            book_info[edition_number] = isbn
    return book_info