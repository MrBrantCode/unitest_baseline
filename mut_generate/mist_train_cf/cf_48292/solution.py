"""
QUESTION:
Write a function `rearrange_string(s)` that takes a string `s` as input and rearranges its characters such that all numeric characters appear first, followed by all alphabetic characters. The original order of numeric and alphabetic characters should be preserved.
"""

def rearrange_string(s):
    numeric_chars = [char for char in s if char.isdigit()]
    alphabetic_chars = [char for char in s if char.isalpha()]

    
    return "".join(numeric_chars + alphabetic_chars)