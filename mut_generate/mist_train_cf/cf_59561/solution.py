"""
QUESTION:
Create a function `reverse_and_capitalize` that accepts an array of strings. The function should return the array with its elements in reverse order and each character in every string capitalized and reversed.
"""

def reverse_and_capitalize(array):
    return [item[::-1].upper() for item in array[::-1]]