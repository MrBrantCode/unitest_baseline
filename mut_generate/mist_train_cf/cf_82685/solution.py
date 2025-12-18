"""
QUESTION:
Eliminate repetitive elements in a 2D array of integers while maintaining the original order of subarrays. Implement a function `eliminate_repetitive(arr)` that takes a 2D array `arr` as input and returns a new 2D array where each subarray contains unique integers.
"""

def eliminate_repetitive(arr):
    found_elements = set()
    new_arr = []
    for sub_arr in arr:
        new_sub_arr = []
        for num in sub_arr:
            if num not in found_elements:
                new_sub_arr.append(num)
                found_elements.add(num)
        new_arr.append(new_sub_arr)
    return new_arr