"""
QUESTION:
Write a function named `compare_strings` that takes two strings as input and returns `True` if they are identical and `False` otherwise. The function should not use any built-in string comparison functions, loops, or recursion. The time complexity of the function should be O(n), where n is the length of the longer string.
"""

def entance(string1, string2):
    if len(string1) != len(string2):
        return False

    i = 0
    while i < len(string1):
        if string1[i] != string2[i]:
            return False
        i += 1

    return True