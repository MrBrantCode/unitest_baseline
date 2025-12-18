"""
QUESTION:
Write a function `append_and_remove_duplicates(str1, str2)` that takes two strings `str1` and `str2` as parameters and returns a new string. The new string should have the characters of `str2` appended to `str1`, and all duplicate characters should be removed.
"""

def append_and_remove_duplicates(str1, str2):
    # Append the characters of str2 to str1
    result = str1 + str2

    # Remove duplicate characters using a set
    result = ''.join(set(result))

    return result