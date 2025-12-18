"""
QUESTION:
Construct a function named `sort_by_binary_len` that takes an array of positive integers as input and returns the array sorted in ascending order based on the length of the binary representation of each integer. In cases where the binary lengths are equal, the integers should be sorted in ascending order of their decimal values. The binary representation length should exclude the '0b' prefix.
"""

def sort_by_binary_len(arr):
    return sorted(arr, key=lambda x: (len(bin(x))-2, x))