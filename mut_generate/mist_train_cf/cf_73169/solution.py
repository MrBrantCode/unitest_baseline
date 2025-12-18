"""
QUESTION:
Write a function called `find_median` that takes a list of integers as input, sorts them in ascending order, and returns the middle value. The list may have an odd number of elements.
"""

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    middle_index = len(sorted_numbers) // 2
    return sorted_numbers[middle_index]