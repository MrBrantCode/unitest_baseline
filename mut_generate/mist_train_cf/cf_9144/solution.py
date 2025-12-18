"""
QUESTION:
Write a function named `reverse_concatenate` that takes two strings as input and returns a new string. The function should concatenate the input strings with a space in between and then reverse the order of characters in the resulting string.
"""

def reverse_concatenate(str1, str2):
    concatenated = str1 + ' ' + str2
    reversed_concatenated = concatenated[::-1]
    return reversed_concatenated