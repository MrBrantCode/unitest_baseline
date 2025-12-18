"""
QUESTION:
Create a function named `reverse_strings` that takes a list of strings as input and returns a new list with the order of characters in each string reversed.
"""

def reverse_strings(list_of_strings):
    return [s[::-1] for s in list_of_strings]