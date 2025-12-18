"""
QUESTION:
Create a function `sum_within_bounds` that takes in a list of integers, a lower bound, and an upper bound. The function should return `True` if the sum of all elements in the list and the sum of the first half of the list are both within the specified bounds. The function should only consider lists with an even number of elements.
"""

def sum_within_bounds(nums, lower, upper):
    if len(nums) % 2 != 0:  
        return False
    half_sum = sum(nums[:len(nums)//2])
    full_sum = sum(nums)
    return lower <= half_sum <= upper and lower <= full_sum <= upper