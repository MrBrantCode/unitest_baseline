"""
QUESTION:
Create a Python function named `sort_strings` that takes a list of strings as input and returns a new list with the strings sorted in alphabetical order. Additionally, the characters within each string should also be sorted in alphabetical order. The function should perform case-insensitive sorting, treating uppercase and lowercase letters as the same. The function can modify the case of the characters in the output strings as necessary to achieve the desired sorting.
"""

def sort_strings(lst):
    return [''.join(sorted(word.lower())) for word in sorted(lst, key=str.lower)]