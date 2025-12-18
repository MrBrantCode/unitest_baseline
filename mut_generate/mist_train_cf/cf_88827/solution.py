"""
QUESTION:
Implement a function `sort_strings` that takes an array of strings as input and returns the array sorted in descending order of the number of vowels in each string. If two strings have the same number of vowels, they should be sorted alphabetically. The function should handle arrays with duplicate strings.
"""

def sort_strings(array):
    array = sorted(array, key=lambda x: (-sum(1 for char in x if char.lower() in 'aeiou'), x))
    return array