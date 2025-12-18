"""
QUESTION:
Write a function `all_substrings` that generates all substrings of a given string in descending order of their lengths, excluding the restriction on the order of substrings with the same length. The function should take one string argument and return a list of all substrings.
"""

def all_substrings(input_string):
    length = len(input_string)
    return [input_string[i: j] for i in range(length) for j in range(i + 1, length + 1)]