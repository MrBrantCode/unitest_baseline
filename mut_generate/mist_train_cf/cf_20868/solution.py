"""
QUESTION:
Combine a list of strings into a single string while removing duplicates.

Create a function `combine_strings` that takes a list of strings as input and returns a concatenated string. The function should remove any duplicate strings from the list before concatenating them. If the list is empty, the function should return an empty string. The function should be able to handle lists with up to 100 strings, each with up to 50 characters. The order of the strings in the output string does not matter.
"""

def combine_strings(strings):
    unique_strings = list(set(strings))
    return ' '.join(unique_strings) if unique_strings else ''