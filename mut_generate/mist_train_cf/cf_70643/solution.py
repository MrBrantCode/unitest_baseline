"""
QUESTION:
Write a function `reverse_strings` that takes a list of strings as input, reverses each string in the list, and returns the list of reversed strings. The function should handle Unicode characters and preserve the original character case of each string. Do not use the built-in `reverse()` function.
"""

def reverse_strings(input_list):
    reversed_list = [single_string[::-1] for single_string in input_list]
    return reversed_list