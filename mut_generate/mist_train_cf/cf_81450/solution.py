"""
QUESTION:
Given two strings `s1` and `s2` with the same length, implement a function `checkIfCanBreak` that checks if some permutation of `s1` can break some permutation of `s2` or vice versa. The function should return `True` if such a permutation exists, and `False` otherwise.

A string `x` can break string `y` if `x[i] >= y[i]` for all `i` between `0` and `n-1`, where `n` is the length of the strings. The input strings consist of lowercase English letters.
"""

def checkIfCanBreak(s1: str, s2: str) -> bool:
    s1, s2 = sorted(s1), sorted(s2)
    return all(s1[i] >= s2[i] for i in range(len(s1))) or all(s2[i] >= s1[i] for i in range(len(s2)))