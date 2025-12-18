"""
QUESTION:
Write a function named `find_maximum` that takes a list of integers as input and returns the maximum number(s) in the list. If the input list is empty or contains non-integer elements, the function should return `None`. If the list contains duplicate maximum numbers, the function should return a list of all the duplicate maximum numbers.
"""

def find_maximum(lst):
    # Check if list is empty
    if not lst:
        return None

    # Check if list contains non-integer elements
    if not all(isinstance(x, int) for x in lst):
        return None

    # Find maximum number
    maximum = max(lst)

    # Find all duplicate maximum numbers
    duplicates = [x for x in lst if x == maximum]

    return duplicates