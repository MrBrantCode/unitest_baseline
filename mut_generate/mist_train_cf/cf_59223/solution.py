"""
QUESTION:
Write a function `rearrange_letters` that takes a string `s` as input and returns a rearranged string such that the first half contains only uppercase letters and the second half contains only lowercase letters. The letters should appear in the order they were originally placed in respect to other letters of the same case.
"""

def rearrange_letters(s):
    upper_chars = [c for c in s if c.isupper()]
    lower_chars = [c for c in s if c.islower()]
    return "".join(upper_chars + lower_chars)