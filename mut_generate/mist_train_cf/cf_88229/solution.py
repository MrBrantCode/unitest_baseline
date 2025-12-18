"""
QUESTION:
Write a function named `is_permutation` that checks if the given string `str1` is a permutation of the string `str2`. The function should consider only alphabetic characters and ignore case. It should handle strings with different lengths and strings containing special characters and spaces. The function should have a time complexity of O(n log n), where n is the length of the longer string, and use only constant extra space.
"""

def is_permutation(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = ''.join(c for c in str1 if c.isalpha())
    str2 = ''.join(c for c in str2 if c.isalpha())
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)