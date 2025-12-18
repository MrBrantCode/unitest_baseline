"""
QUESTION:
Write a function named `compute_aggregate` that takes an array of numbers as input and returns the sum of the cubes of each number in the array.
"""

def compute_aggregate(arr):
    total_sum = 0
    for i in arr:
        total_sum += i**3
    return total_sum