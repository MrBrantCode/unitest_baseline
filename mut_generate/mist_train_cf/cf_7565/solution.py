"""
QUESTION:
Write a function `sum_of_two_largest_numbers` that takes an array of positive integers with a length of at least four as input and returns the sum of the two largest integers in the array.
"""

def sum_of_two_largest_numbers(arr):
    arr.sort()  # Sort the array in ascending order
    return arr[-1] + arr[-2]  # Return the sum of the last two elements