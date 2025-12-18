"""
QUESTION:
Write a function `sum_of_squares(arr)` that takes an array of integers as input and returns the sum of the squares of all positive numbers in the array. The array elements are integers between -100 and 100 and the array size is limited to a maximum of 1000 elements. If the array does not contain any positive numbers, the function should return 0.
"""

def sum_of_squares(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num ** 2
    return total