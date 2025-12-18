"""
QUESTION:
Create a function `reverse_string` that takes a string `s` as input, reverses its order while excluding numerical values and special characters, ignores whitespace, and is case-insensitive. The function should have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    s = s.lower()
    s = ''.join(e for e in s if e.isalpha() or e.isspace())
    s = s.replace(" ", "")   
    return s[::-1]