"""
QUESTION:
Write a function named `is_permutation` that takes two strings `str1` and `str2` as input and returns `True` if `str1` is a permutation of `str2` considering only alphabetic characters and ignoring case, and `False` otherwise. The function should have a time complexity of O(n) where n is the length of the longer string.
"""

def is_permutation(str1, str2):
    str1 = ''.join(filter(str.isalpha, str1.lower()))
    str2 = ''.join(filter(str.isalpha, str2.lower()))

    if len(str1) != len(str2):
        return False

    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    for count in char_count.values():
        if count != 0:
            return False

    return True