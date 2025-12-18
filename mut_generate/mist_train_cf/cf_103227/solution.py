"""
QUESTION:
Create a function called `filter_odd_divisible_by_three` that takes an array of integers as input and returns a new array containing only the numbers that are even and not divisible by 3, sorted in ascending order.
"""

def filter_odd_divisible_by_three(array):
    return sorted([num for num in array if num % 2 == 0 and num % 3 != 0])