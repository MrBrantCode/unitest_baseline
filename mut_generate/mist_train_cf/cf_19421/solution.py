"""
QUESTION:
Create a function called `is_rotation` that takes two strings and their corresponding lengths as parameters. The function should return True if the second string is a rotation of the first string and False otherwise. The strings are considered rotations of each other if one can be obtained by shifting all characters of the other by a certain number of positions and wrapping around to the beginning. Assume that the input strings only contain ASCII characters and that the input lengths are non-negative integers.
"""

def is_rotation(s1, s2, n1, n2):
    return n1 == n2 and s2 in s1 + s1