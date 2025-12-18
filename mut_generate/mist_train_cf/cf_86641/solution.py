"""
QUESTION:
Create a function `double_array(arr)` that takes an array of integers, doubles each number in the array, removes any duplicates, and returns the resulting array sorted in non-decreasing order. The input array can contain both positive and negative integers and can be up to 10^6 elements in size.
"""

def double_array(arr):
    result = set()
    for num in arr:
        result.add(num * 2)
    return sorted(list(result))