"""
QUESTION:
Write a function called `longest_common_contiguous_subarray` that takes two sorted integer arrays as input and returns the length of the longest common contiguous subarray. The function should have a time complexity of O(n) and space complexity of O(1).
"""

def longest_common_contiguous_subarray(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    
    max_len = 0
    current_len = 0
    
    i = 0
    j = 0
    
    while i < len1 and j < len2:
        if arr1[i] == arr2[j]:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
            current_len = 0
        else:
            j += 1
            current_len = 0
    
    return max_len