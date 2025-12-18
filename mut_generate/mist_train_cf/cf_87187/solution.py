"""
QUESTION:
Write a function named `sum_elements` that takes a 2D array as input and returns the sum of all elements in the array that are greater than 5 and less than 15, excluding any elements that are divisible by both 2 and 3.
"""

def sum_elements(array):
    """Returns the sum of all elements in the 2D array that are greater than 5 and less than 15,
    excluding any elements that are divisible by both 2 and 3."""
    total_sum = 0
    for sublist in array:
        for element in sublist:
            if 5 < element < 15 and not (element % 2 == 0 and element % 3 == 0):
                total_sum += element
    return total_sum