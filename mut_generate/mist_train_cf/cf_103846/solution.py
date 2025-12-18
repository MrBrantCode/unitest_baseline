"""
QUESTION:
Write a function named `find_largest_smallest` that takes a list of integers as input and returns a tuple containing the largest and smallest numbers in the list. If the input list is empty, the function should return `None`.
"""

def find_largest_smallest(numbers):
    if len(numbers) == 0:
        return None
    else:
        largest = max(numbers)
        smallest = min(numbers)
        return (largest, smallest)