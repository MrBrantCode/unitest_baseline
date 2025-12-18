"""
QUESTION:
Write a function `find_largest_smallest` that takes a list of numbers as input and returns a tuple containing the largest and smallest numbers in the list. If the list is empty, the function should return `None`. The list may contain duplicates.
"""

def find_largest_smallest(numbers):
    if len(numbers) == 0:
        return None
    else:
        largest = max(numbers)
        smallest = min(numbers)
        return (largest, smallest)