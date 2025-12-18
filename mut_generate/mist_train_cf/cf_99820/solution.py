"""
QUESTION:
Create a function that applies a complex mathematical formula to each element in a given list of integers and returns the new list. The formula is `num ** 2 + 2 * num + 1`. The input list should remain unchanged.
"""

def entrance(nums):
    return list(map(lambda num: num ** 2 + 2 * num + 1, nums))