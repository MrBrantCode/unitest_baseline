"""
QUESTION:
Write a function `cube_positive_integers` that accepts a list of integers, removes duplicates and negative integers, and returns a list of cubes of the remaining positive integers in ascending order with a time complexity of O(n).
"""

def cube_positive_integers(nums):
    positive_nums = set(num for num in nums if num > 0)
    return sorted(num**3 for num in positive_nums)