"""
QUESTION:
Write a function `calculate_sum` that takes an array of integers as an argument and returns the sum of its elements. The function should be able to handle arrays of any size, and it should only use a single loop to iterate through the array, without utilizing any built-in functions or libraries for calculating the sum.
"""

def entrance(arr):
    total = 0
    for num in arr:
        total += num
    return total