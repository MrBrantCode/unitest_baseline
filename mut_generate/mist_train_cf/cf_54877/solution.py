"""
QUESTION:
Create a function `is_subsequence(str1, str2)` that determines whether `str1` is a subsequence of `str2`. The function should return `True` if `str1` is a subsequence of `str2` (i.e., all characters of `str1` appear in the same order in `str2`) and `False` otherwise. The function should only consider the characters in `str1` and `str2`, ignoring any other factors.
"""

def entrance(str1, str2):
    # Initialize trackers for both strings
    i = j = 0

    # Get length of both strings
    m = len(str1)
    n = len(str2)

    # Traverse str1 and str2
    while i < m and j < n:
        # If characters match, increment str1 tracker
        if str1[i] == str2[j]:
            i += 1
        # Always increment str2 tracker
        j += 1

    # If all characters of str1 were found in str2 in order
    return i == m