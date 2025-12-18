"""
QUESTION:
Write a function named `sum_of_cubes_in_range` that takes a vector of integers, a minimum value, and a maximum value as input. The function should calculate the sum of the cubes of all elements in the vector and return `true` if the sum is within the range defined by the minimum and maximum values, and `false` otherwise.
"""

def sum_of_cubes_in_range(nums, min_val, max_val):
    sum_of_cubes = sum(i**3 for i in nums)
    return min_val <= sum_of_cubes <= max_val