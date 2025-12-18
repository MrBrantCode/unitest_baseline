"""
QUESTION:
Create a function named `alphabetize_string` that takes a string as input and returns a new string where all alphabetic characters are in alphabetical order, while non-alphabetic characters remain in their original positions. The function should only rearrange the alphabetic characters and leave other characters (such as spaces and punctuation marks) unchanged.
"""

def alphabetize_string(s):
    sorted_chars = sorted([c for c in s if c.isalpha()])
    result = ''
    for c in s:
        result += sorted_chars.pop(0) if c.isalpha() else c
    return result