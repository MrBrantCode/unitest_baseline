"""
QUESTION:
Function `findLUSSize(a, b)` should be implemented to find the length and count of the longest uncommon subsequence between two strings `a` and `b`. The function should return a tuple of two integers. If the longest uncommon subsequence does not exist, the function should return `-1` for the length and `0` for the count. The strings `a` and `b` consist of lower-case English letters and their lengths are between `1` and `100`.
"""

def findLUSSize(a, b):
    if a == b:
        return -1, 0
    else:
        return max(len(a), len(b)), 2