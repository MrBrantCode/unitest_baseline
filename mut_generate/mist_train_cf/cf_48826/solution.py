"""
QUESTION:
Develop a function `sort_array` that takes a list of alphanumeric strings as input, where each string contains a combination of digits and letters, and returns the sorted list in ascending order of the numerical value of the strings. If two strings have the same numerical value, they should be sorted lexicographically (in alphabetical order).
"""

def sort_array(arr):
    return sorted(arr, key=lambda x: (int(''.join(filter(str.isdigit, x))), x))