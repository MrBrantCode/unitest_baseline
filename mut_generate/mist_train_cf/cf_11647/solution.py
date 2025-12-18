"""
QUESTION:
Write a function `remove_occurrences` that takes a list of integers as input and returns a new list with all occurrences of the number 4 removed.
"""

def remove_occurrences(nums):
    return [num for num in nums if num != 4]