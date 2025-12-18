"""
QUESTION:
Given two integer arrays, determine if it is possible to exchange elements between them to make the first array consist only of even numbers while preserving the overall sum across both arrays. The function should return "YES" if it is possible and "NO" otherwise. The function should be named `modification` and should work with input arrays containing at least one integer.
"""

def modification(lst1, lst2):
    total_sum = sum(lst1) + sum(lst2)
    if total_sum % 2 != 0:
        return "NO"
    else:
        return "YES"