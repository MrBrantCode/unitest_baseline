"""
QUESTION:
Create a function called `calculate_sum` that takes an array of integers as input, including possible negative numbers, and returns the sum of all the values in the array. The function should be able to handle arrays containing both positive and negative integers.
"""

def calculate_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total