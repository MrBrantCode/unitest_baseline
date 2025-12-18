"""
QUESTION:
Develop a function named `find_smallest_common_index` that takes two arrays of integers as input and returns the index of the first occurrence of the smallest common element in the first array. If there is no common element, return -1. The function should handle arrays of different lengths, negative integers, duplicate elements, and large input sizes efficiently.
"""

def find_smallest_common_index(array1, array2):
    smallest_common = None
    common_index = -1
    
    for i, num in enumerate(array1):
        if num in array2:
            if smallest_common is None or num < smallest_common:
                smallest_common = num
                common_index = i
                
    return common_index