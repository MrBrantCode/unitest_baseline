"""
QUESTION:
Define a function named `common_chars` that takes two strings `str1` and `str2` as arguments and returns a string composed of the unique characters that appear in both strings, without preserving their original order and without duplicates.
"""

def common_chars(str1, str2):
    return ''.join(set(str1) & set(str2))