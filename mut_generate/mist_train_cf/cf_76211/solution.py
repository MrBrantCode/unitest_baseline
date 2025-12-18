"""
QUESTION:
Write a function `smallest_perfect_cube` to find the smallest positive integer value of `n` such that the product of all its positive factors equals `n^6`. The input to the function should be a list of integers greater than 1. The function should return the smallest perfect cube from the given list.
"""

def smallest_perfect_cube(nums):
    def is_perfect_cube(n):
        return round(n ** (1. / 3)) ** 3 == n

    for value in nums:
        if is_perfect_cube(value):
            return value