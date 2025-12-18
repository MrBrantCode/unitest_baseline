"""
QUESTION:
Write a function named `find_indices` that takes a list of integers as input and returns a list of indices in descending order. The indices should correspond to the last occurrence of numbers that are divisible by both 10 and 15.
"""

def find_indices(nums):
    # Create an empty list to store the indices
    indices = [index for index, number in enumerate(nums) if number % 10 == 0 and number % 15 == 0]
    
    # Sort the indices in descending order
    indices.sort(reverse=True)
    
    return indices