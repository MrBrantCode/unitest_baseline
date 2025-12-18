"""
QUESTION:
Write a function `cube_positive_integers` that accepts a list of integers, removes duplicates and negative integers, cubes the remaining positive integers, and returns the cubes in ascending order with a time complexity of O(n).
"""

def cube_positive_integers(nums):
    positive_nums = set(num for num in nums if num > 0)
    cubes = sorted(num**3 for num in positive_nums)
    return cubes