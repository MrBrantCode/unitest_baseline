"""
QUESTION:
Write a function `compare_strings(s1, s2)` that compares two strings and returns `True` if they are equal, considering case sensitivity and ignoring leading and trailing white spaces. The function should be implemented using recursion and should not use any built-in string comparison methods or functions.
"""

def compare_strings(s1, s2):
    # Base case: if both strings are empty, they are considered equal
    if len(s1) == 0 and len(s2) == 0:
        return True

    # Ignore leading and trailing white spaces
    if len(s1) > 0 and s1[0] == ' ':
        return compare_strings(s1[1:], s2)
    if len(s1) > 0 and s1[-1] == ' ':
        return compare_strings(s1[:-1], s2)
    if len(s2) > 0 and s2[0] == ' ':
        return compare_strings(s1, s2[1:])
    if len(s2) > 0 and s2[-1] == ' ':
        return compare_strings(s1, s2[:-1])

    # If the first characters are not equal, the strings are considered different
    if s1[0] != s2[0]:
        return False

    # Recursive call to compare the remaining characters
    return compare_strings(s1[1:], s2[1:])