"""
QUESTION:
Create a function `double_and_sort_array` that takes an array of integers as input, doubles the value of each number, removes duplicates, and returns the resulting array sorted in non-decreasing order. The input array can contain up to 10^6 elements, including both positive and negative integers.
"""

def double_and_sort_array(arr):
    unique_elements = set()
    
    for num in arr:
        unique_elements.add(num * 2)
    
    return sorted(list(unique_elements))