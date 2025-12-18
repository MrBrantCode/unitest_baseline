"""
QUESTION:
Write a function called `find_smallest_number` that takes a list of integers as input and returns the smallest positive integer in the list. If the list is empty, return "Error: The list is empty." If all numbers in the list are negative, return "Error: There are no positive numbers in the list." The function should exclude negative numbers from the calculation.
"""

def find_smallest_number(lst):
    # Check if the list is empty
    if len(lst) == 0:
        return "Error: The list is empty."

    # Initialize the smallest number as positive infinity
    smallest = float('inf')

    # Iterate over each number in the list
    for num in lst:
        # Exclude negative numbers
        if num < 0:
            continue

        # Update the smallest number if a smaller positive number is found
        if num < smallest:
            smallest = num

    # Check if all numbers in the list were negative
    if smallest == float('inf'):
        return "Error: There are no positive numbers in the list."

    return smallest