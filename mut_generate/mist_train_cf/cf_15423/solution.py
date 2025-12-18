"""
QUESTION:
Write a function `reverse_concatenate` that takes two strings as input, concatenates them with a space in between, reverses the order of characters, and removes any duplicate characters from the resulting string.
"""

def reverse_concatenate(string1, string2):
    concatenated = string1 + ' ' + string2
    reversed_string = concatenated[::-1]
    unique_string = ''.join(set(reversed_string))
    return unique_string