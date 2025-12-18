"""
QUESTION:
Write a function `count_unique_chars` that takes two strings `str1` and `str2` as input and returns the number of unique characters that appear in both strings. The function must have a time complexity of O(n), where n is the length of the longer string, and cannot use loops for character comparison or the intersection operation. It should utilize Python's built-in data structures.
"""

def count_unique_chars(str1, str2):
    unique_chars_str1 = set(str1)
    unique_chars_str2 = set(str2)
    common_chars = unique_chars_str1 & unique_chars_str2
    return len(common_chars)