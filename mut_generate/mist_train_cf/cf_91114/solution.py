"""
QUESTION:
Write a function named `sort_strings_by_length` that takes an array of strings as input and returns the array sorted in descending order based on the length of each string.
"""

def sort_strings_by_length(arr):
    arr.sort(key=lambda x: len(x), reverse=True)
    return arr