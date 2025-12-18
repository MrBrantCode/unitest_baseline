"""
QUESTION:
Write a function `long_com_subarr(arr1, arr2)` that finds the length of the longest common contiguous subarray between two integer arrays `arr1` and `arr2`. The function should take two lists of integers as input and return the length of the longest common contiguous subarray.
"""

def long_com_subarr(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    res = 0
    count = 0 
    
    for i in range(len1):
        for j in range(len2):
            if arr1[i] == arr2[j]:
                count += 1
            else: 
                if res < count:
                    res = count
                count = 0
    
    return res