"""
QUESTION:
Write a function `sort_by_binary_len` that sorts a list of positive integers based on the length of their binary representation in ascending order. If two or more integers have the same binary length, they should be sorted based on their decimal values. The function should return the sorted list of integers. The input list will only contain positive integers.
"""

def sort_by_binary_len(arr):
    return sorted(arr, key=lambda x: (len(bin(x))-2, x))