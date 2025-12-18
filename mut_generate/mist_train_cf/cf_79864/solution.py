"""
QUESTION:
Write a function `sort_by_binary_ones_zeros_desc(arr)` that sorts a list of integers based on the count of 1s in their binary representation in ascending order, then by the count of 0s in ascending order, and finally by their decimal values in descending order. The function should work with both positive and negative integers.
"""

def sort_by_binary_ones_zeros_desc(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), bin(x).count('0'), -x))
    return arr