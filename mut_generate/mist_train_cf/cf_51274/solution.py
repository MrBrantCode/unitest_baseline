"""
QUESTION:
Write a function `is_subsequence(str1, str2)` that checks if `str1` exists as a subsequence within `str2`. The function should return `True` if `str1` is a subsequence of `str2` and `False` otherwise. The function should consider all possible variations and sequences of character placements within `str2`.
"""

def entrance(str1, str2):
    i = j = 0
    len1 = len(str1)
    len2 = len(str2)

    while j < len1 and i < len2:
        if str1[j] == str2[i]:
            j += 1
        i += 1

    return j == len1