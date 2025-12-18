"""
QUESTION:
Write a function named `append_and_remove_duplicates` that takes two strings `str1` and `str2` as parameters and returns a new string. The function should append the characters of `str2` to `str1` and then remove any duplicate characters from the resulting string.
"""

def append_and_remove_duplicates(str1, str2):
    # Append the characters of str2 to str1
    result = str1 + str2

    # Remove duplicate characters using a set
    result = ''.join(set(result))

    return result