"""
QUESTION:
Develop a function named `sort_by_binary_len` that takes an array of positive integers as input. Sort the array in ascending order based on the length of the binary representation of each integer. If two or more integers have the same binary length, sort them according to their decimal values.
"""

def sort_by_binary_len(arr):
    return sorted(arr, key=lambda x: (len(bin(x)[2:]), x))