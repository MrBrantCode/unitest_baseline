"""
QUESTION:
Write a function named `sort_func` that sorts a given list of alphanumeric strings in ascending order of their numerical value. When the numerical values are equal, the sorting should be in descending order of their alphabetical value, ignoring case sensitivity.
"""

def sort_func(arr):
    return sorted(arr, key=lambda x: (int(''.join(filter(str.isdigit, x))), ''.join(filter(str.isalpha, x)).lower()[::-1]), 
                  reverse=False)