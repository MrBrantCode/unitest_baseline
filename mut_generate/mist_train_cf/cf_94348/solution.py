"""
QUESTION:
Write a function `find_max` that takes a list of integers as input and returns the maximum value in the list without using the built-in `max()` function. The list may contain negative numbers and may be empty. If the list is empty, the function should return `None`.
"""

def find_max(lst):
    # Check if the list is empty
    if len(lst) == 0:
        return None

    # Initialize the maximum value with the first element
    maximum = lst[0]

    # Iterate through the list starting from the second element
    for num in lst[1:]:
        # Compare the current element with the maximum value
        if num > maximum:
            maximum = num

    return maximum