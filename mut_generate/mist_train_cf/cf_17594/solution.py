"""
QUESTION:
Write a function `get_even_indices` that takes a list of integers as input and returns a list of indices of all even numbers in the array in ascending order. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def get_even_indices(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            result.append(i)
    return result