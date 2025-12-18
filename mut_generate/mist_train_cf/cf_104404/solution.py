"""
QUESTION:
Write a function named `sum_of_squares` that takes an array of integers and non-integers as a parameter. The function should return the sum of the squares of all the positive integers in the array. If an element is not a positive integer, it should be ignored.
"""

def sum_of_squares(arr):
    total_sum = 0
    for num in arr:
        if isinstance(num, int) and num > 0:
            total_sum += num ** 2
    return total_sum