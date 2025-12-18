"""
QUESTION:
Create a function called `is_rotation` that takes two strings and their corresponding lengths as input. Return `True` if the second string is a rotation of the first string, and `False` otherwise. A rotation is defined as shifting all the characters of a string by a certain number of positions and wrapping around to the beginning. The function should assume that the input lengths are non-negative integers.
"""

def is_rotation(string1, string2, length1, length2):
    if length1 != length2:
        return False
    if string2 in (string1 + string1):
        return True
    return False