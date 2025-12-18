"""
QUESTION:
Write a function `modify_casing(s)` that takes a string `s` as input and returns a string where each character is modified based on its ASCII value. If the ASCII value of the character is even, the character should be upper case. If its ASCII value is odd, the character should be in lower case. The function should handle all characters, including punctuation and whitespace.
"""

def modify_casing(s):
    new_str = ""
    for c in s:
        if ord(c) % 2 == 0:
            new_str += c.upper()
        else:
            new_str += c.lower()
    return new_str