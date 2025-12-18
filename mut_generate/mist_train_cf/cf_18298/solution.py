"""
QUESTION:
Create a function `sort_array` that takes an array of string elements as input. Sort the array such that numbers (if present) appear first in ascending order, followed by the strings in alphabetical order, and then any special characters in ascending order. The function should return the sorted array.
"""

def sort_array(arr):
    numbers = [elem for elem in arr if elem.isdigit()]
    strings = [elem for elem in arr if elem.isalpha()]
    special_characters = [elem for elem in arr if not elem.isdigit() and not elem.isalpha()]
    
    return sorted(numbers) + sorted(strings) + sorted(special_characters)