"""
QUESTION:
Write a function called `sort_strings` that takes an array of strings as input and returns the array sorted in ascending order based on the number of distinct characters in each string. If two or more strings have the same number of distinct characters, they should be sorted lexicographically.
"""

def sort_strings(arr):
    return sorted(arr, key=lambda x: (len(set(x)), ''.join(sorted(x))))