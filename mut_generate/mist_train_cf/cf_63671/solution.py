"""
QUESTION:
Create a function named `sort_strings` that takes an array of strings as input and returns the array sorted in descending order based on the length of the strings.
"""

def sort_strings(array):
    return sorted(array, key=len, reverse=True)