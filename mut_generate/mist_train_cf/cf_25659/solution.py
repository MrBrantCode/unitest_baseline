"""
QUESTION:
Develop a function `filter_negative_numbers` that takes a list of integers as input and returns a new list containing only the non-negative numbers from the original list. The function should not modify the original list.
"""

def filter_negative_numbers(nums):
    # return only positive numbers
    return [num for num in nums if num >= 0]