"""
QUESTION:
Write a function is_strictly_ascending to determine if a given list of integers is strictly ascending. A list is strictly ascending if each element is greater than the previous element. The function should return True if the list is strictly ascending, otherwise return False.
"""

def is_strictly_ascending(nums):
    return all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))