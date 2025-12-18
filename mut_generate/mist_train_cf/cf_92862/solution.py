"""
QUESTION:
Define a function `is_anagram(str1, str2)` that takes two strings as input and returns a boolean value. The function should determine if `str1` is an anagram of `str2`, ignoring case, whitespace, and character order. The function should return `True` if `str1` is an anagram of `str2` and `False` otherwise.
"""

def is_anagram(str1, str2):
    # Remove whitespace and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort the strings alphabetically
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare the sorted strings
    return sorted_str1 == sorted_str2