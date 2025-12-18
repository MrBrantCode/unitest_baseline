"""
QUESTION:
Create a function named `double_and_sort` that takes an array of integers as input and returns a new array where all numbers in the input array are doubled and sorted in non-decreasing order. The input array can contain both positive and negative integers and its size can be up to 10^6 elements.
"""

def double_and_sort(arr):
    return sorted([num * 2 for num in arr])