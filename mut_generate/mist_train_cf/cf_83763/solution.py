"""
QUESTION:
Design a function called `sort_by_binary_len` that takes an array of positive integers and returns a sorted array in ascending order. The sorting order is determined by the length of the binary equivalents of these integers; if multiple integers have the same binary length, their numerical (decimal) representation is used for sorting.
"""

def sort_by_binary_len(arr):
    arr.sort(key=lambda x: (len(bin(x))-2, x))
    return arr