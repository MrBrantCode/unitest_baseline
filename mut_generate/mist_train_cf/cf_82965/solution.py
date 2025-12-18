"""
QUESTION:
Write a function `replace_vowels_with_dollar(s)` that takes a string `s` as input and returns the string with all vowels (both lowercase and uppercase) replaced with the character '$'.
"""

def replace_vowels_with_dollar(s):
    trans = str.maketrans('aeiouAEIOU', '$$$$$$$$$$')
    return s.translate(trans)