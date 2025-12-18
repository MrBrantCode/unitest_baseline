"""
QUESTION:
Write a function `compute_median(numbers)` to calculate the median of a set of integers. The function should take a list of integers as input, sort the numbers in ascending order, and then determine the median based on whether the number of elements is odd or even. The function should return the median value.
"""

def compute_median(numbers):
    sorted_numbers = sorted(numbers)  # Sort the numbers in ascending order

    n = len(sorted_numbers)
    if n % 2 == 0:  # If there are even number of elements
        middle_right = n // 2
        middle_left = middle_right - 1
        median = (sorted_numbers[middle_left] + sorted_numbers[middle_right]) / 2
    else:  # If there are odd number of elements
        middle = n // 2
        median = sorted_numbers[middle]

    return median