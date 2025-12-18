"""
QUESTION:
Write a function named `sum_of_squares` that calculates the sum of the squares of all positive integers in a given array of integers. The array can contain up to 1000 elements, each ranging from -100 to 100. If the array does not contain any positive numbers, the function should return 0.
"""

def sum_of_squares(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num ** 2
    return total