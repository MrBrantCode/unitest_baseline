"""
QUESTION:
Write a function named `move_zeros` that takes a list of integers as input and returns a new list with all zeros moved to the end, while maintaining the relative order of non-zero elements. The function should not modify the original input list.
"""

def move_zeros(arr):
    non_zeros = [num for num in arr if num != 0]
    zeros = [0] * (len(arr) - len(non_zeros))
    return non_zeros + zeros