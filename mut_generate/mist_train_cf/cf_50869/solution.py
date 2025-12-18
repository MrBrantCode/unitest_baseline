"""
QUESTION:
Write a function called `check_strings` that takes two strings `s1` and `s2` as inputs. The function should first verify that both strings only contain printable ASCII characters. If this condition is met, it should then determine if `s1` is a permutation of `s2`, considering case sensitivity and whitespace as significant. If the strings do not meet the ASCII requirement, the function should return a corresponding message. If the strings meet the ASCII requirement but are not permutations of each other, the function should return a corresponding message. Otherwise, it should return a message confirming that the strings are permutations of each other.
"""

import string

def check_strings(s1, s2):
    if not all(c in string.printable for c in s1) or not all(c in string.printable for c in s2):
        return "Input strings must only consist of printable ASCII characters."
    if sorted(s1) != sorted(s2):
        return "These strings are not permutations of each other."
    return "These strings are permutations of each other."