"""
QUESTION:
Write a function `sort_strings_by_length_descending` that takes an array of strings as input, filters out strings with lengths less than 3, and returns the remaining strings sorted in descending order of their lengths.
"""

def sort_strings_by_length_descending(arr):
    return sorted([string for string in arr if len(string) >= 3], key=len, reverse=True)