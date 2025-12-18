"""
QUESTION:
Write a function named `find_first_occurrence` that takes a list of strings and a target string as input, and returns the index of the first occurrence of the target string in the list. If the target string is not found, return -1.
"""

def find_first_occurrence(list, string):
    for i, element in enumerate(list):
        if element == string:
            return i
    return -1  # Return -1 if the input string is not found in the list