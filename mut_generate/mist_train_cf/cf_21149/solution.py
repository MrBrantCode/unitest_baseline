"""
QUESTION:
Write a function `concatenate_strings` that takes a list of strings as input and returns a single string that is the concatenation of all the strings in the input list. The input list can contain up to 1000 strings, and each string can have up to 1000 characters. The output string should not have any leading or trailing spaces. If the input list is empty, the function should return an empty string.
"""

def concatenate_strings(strings):
    return ''.join(strings)