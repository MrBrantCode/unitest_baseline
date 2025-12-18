"""
QUESTION:
Write a function `is_reversed` that takes two strings as input and returns `True` if one string is the reverse of the other, and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the strings, and should not use any built-in string reversal functions or methods. The function should handle strings containing special characters, numbers, whitespace, and other non-alphabetic characters.
"""

def is_reversed(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    length = len(string_1)
    for i in range(length):
        if string_1[i] != string_2[length - i - 1]:
            return False
    return True