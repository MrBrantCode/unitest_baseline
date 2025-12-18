"""
QUESTION:
Write a function `find_even_indices` that takes an array of integers as input and returns a list of indices of all even numbers in the array. The array may contain both positive and negative integers.
"""

def find_even_indices(nums):
    return [i for i, num in enumerate(nums) if num % 2 == 0]