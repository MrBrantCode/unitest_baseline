"""
QUESTION:
Implement a function `sort_strings` that sorts an array of strings in descending order of the number of vowels present in each string. If two strings have the same number of vowels, they should be sorted alphabetically. The function should return the sorted array.
"""

def sort_strings(array):
    array = sorted(array, key=lambda x: (-sum(1 for char in x if char.lower() in 'aeiou'), x))
    return array