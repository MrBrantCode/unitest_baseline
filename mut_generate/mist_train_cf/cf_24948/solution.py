"""
QUESTION:
Write a function `compare_strings` that takes two strings `str1` and `str2` as input and returns `True` if they are identical and `False` otherwise. The function should check both the characters and their order. Assume that the input strings only contain ASCII characters.
"""

def entrance(str1, str2):
    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    return True