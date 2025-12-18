"""
QUESTION:
Write a function named `move_zeros` that takes a list of integers as input and returns a new list where all zeros are moved to the end of the list, while maintaining the relative order of the non-zero elements. The length of the output list should be the same as the input list.
"""

def move_zeros(arr):
    non_zeros = [num for num in arr if num != 0]
    zeros = [0] * (len(arr) - len(non_zeros))
    return non_zeros + zeros