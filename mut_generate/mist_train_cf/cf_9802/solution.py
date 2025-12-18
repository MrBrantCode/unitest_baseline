"""
QUESTION:
Write a function called `get_odd_numbers` that takes a list of integers as input and returns a new list containing only the unique odd numbers in descending order.
"""

def get_odd_numbers(nums):
    odd_nums = list(set(filter(lambda x: x % 2 != 0, nums)))
    return sorted(odd_nums, reverse=True)