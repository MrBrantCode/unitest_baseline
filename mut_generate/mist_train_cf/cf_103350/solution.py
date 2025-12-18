"""
QUESTION:
Write a function `is_isogram(s)` that determines if a given string `s` is an isogram. The function should consider both uppercase and lowercase letters, ignore special characters and spaces, and return `True` if the string is an isogram and `False` otherwise. The input string `s` may contain both alphabetic and non-alphabetic characters.
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