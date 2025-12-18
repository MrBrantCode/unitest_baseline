"""
QUESTION:
Write a function named `sum_of_squares` that takes an array of integers as input and returns the sum of the squares of each element in the array. The input array will contain only integers.
"""

def sum_of_squares(arr):
    return sum(x**2 for x in arr)