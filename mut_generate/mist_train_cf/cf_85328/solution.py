"""
QUESTION:
Create a function called `purge_strings` that takes two parameters: a list of strings and a target sequence of characters. The function should return a new list containing only the strings from the original list that do not contain the target sequence.
"""

def purge_strings(strings, sequence):
    return [item for item in strings if sequence not in item]