"""
QUESTION:
Create a function named `is_subsequence` that takes two strings `str1` and `str2` as parameters. The function should return `True` if `str1` is a subsequence of `str2`, meaning all characters of `str1` can be found in the same order in `str2` (possibly with other characters in between), and `False` otherwise.
"""

def is_subsequence(str1, str2):
    i = 0  # Pointer for str1
    j = 0  # Pointer for str2
    
    # Traverse both strings
    while i < len(str1) and j < len(str2):
        # If characters match, move pointer for str2
        if str1[i] == str2[j]:
            i += 1
        # Move pointer for str2
        j += 1
    
    # If we have traversed all characters of str1, it is a subsequence of str2
    return i == len(str1)