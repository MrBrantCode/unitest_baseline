"""
QUESTION:
Write a function `find_smallest_common_index(array1, array2)` that takes two arrays of integers as input and returns the index of the first occurrence of the smallest common element in both arrays. If there is no common element, return -1. The function should handle arrays of different lengths, negative integers, and duplicate elements.
"""

def find_smallest_common_index(array1, array2):
    # Find the smallest common element in both arrays
    smallest_common = float('inf')
    for num in array1:
        if num in array2:
            smallest_common = min(smallest_common, num)
    
    # Find the index of the smallest common element in array1
    if smallest_common == float('inf'):
        return -1
    else:
        return array1.index(smallest_common)