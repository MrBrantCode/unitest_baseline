"""
QUESTION:
Write a function `sort_by_binary_len` that takes an array of strictly positive integers as input and returns the array sorted in ascending order based on the length of the binary representation of each integer. In cases where multiple integers have the same binary length, use their decimal numerical values as a tiebreaker. The function should not include zero as an input value, as it is not a strictly positive integer.
"""

def sort_by_binary_len(arr):
    return sorted(arr, key = lambda x: (len(bin(x)[2:]), x))