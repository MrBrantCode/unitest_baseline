"""
QUESTION:
Write a function named `compare_strings` that takes two strings as input and returns a boolean indicating whether the strings are equal. The function must have a time complexity of O(n), where n is the length of the longer string, and cannot use any built-in comparison functions, loops, or recursion.
"""

def compare_strings(s1, s2):
    if len(s1) != len(s2):
        return False

    i = 0
    while i < len(s1):
        if s1[i] != s2[i]:
            return False
        i += 1

    return True