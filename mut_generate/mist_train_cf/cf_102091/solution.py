"""
QUESTION:
Write a function named `sum_elements` that takes a 2D array as input and returns the sum of all elements that are greater than 5, less than 15, and not divisible by both 2 and 3.
"""

def sum_elements(array_2d):
    total_sum = 0
    for sublist in array_2d:
        for element in sublist:
            if element > 5 and element < 15:
                if element % 2 != 0 or element % 3 != 0:
                    total_sum += element
    return total_sum