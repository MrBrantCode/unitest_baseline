"""
QUESTION:
Create a function `double_and_sort_array(arr)` that takes an array of integers as input. The function should return a new array where each element from the input array is doubled, sorted in non-decreasing order, and contains no duplicate elements. The input array can contain both positive and negative integers and can be up to 10^6 elements in size.
"""

def double_and_sort_array(arr):
    return sorted(set(num * 2 for num in arr))