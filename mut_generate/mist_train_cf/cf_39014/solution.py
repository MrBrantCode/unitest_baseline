"""
QUESTION:
Write a function `two_sum` that takes in two parameters: `nums`, a list of integers, and `target`, an integer. The function should return a list containing the indices of the two numbers in `nums` that add up to `target`. Assume that each input has exactly one solution, and you may not use the same element twice.
"""

def two_sum(nums, target):
    cache = dict()
    for index, value in enumerate(nums):
        if value in cache:
            return sorted([cache[value], index])
        else:
            cache[target - value] = index