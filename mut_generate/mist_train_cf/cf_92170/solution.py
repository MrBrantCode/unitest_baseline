"""
QUESTION:
Create a function `is_isogram(s)` that determines if a given string `s` is an isogram, ignoring case sensitivity and non-alphabetic characters. The function should return `True` if the string is an isogram and `False` otherwise.
"""

def is_isogram(s):
    s = s.lower()
    encountered_chars = set()

    for char in s:
        if char.isalpha():
            if char in encountered_chars:
                return False
            encountered_chars.add(char)

    return True