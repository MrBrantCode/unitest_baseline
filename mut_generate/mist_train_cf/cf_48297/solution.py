"""
QUESTION:
Design a function named `sort_by_binary_len` that takes an array of integers as input. The function should return the array sorted in ascending order based on the lengths of the binary equivalents of the absolute values of the integers. If two integers have the same binary length, they should be sorted based on their absolute decimal values. The original signs of the integers must be preserved in the output.
"""

def sort_by_binary_len(arr):
    return sorted(arr, key=lambda x: (len(bin(abs(x)))-2, abs(x)))