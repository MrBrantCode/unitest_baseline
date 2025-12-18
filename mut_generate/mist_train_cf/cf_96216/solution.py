"""
QUESTION:
Create a function `isSubsequence` that takes two arrays of integers `arr1` and `arr2` as parameters and returns `True` if `arr2` is a subsequence of `arr1`, and `False` otherwise. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. The function should have a time complexity of O(n), where n is the length of the longer array, and space complexity of O(1).
"""

def isSubsequence(arr1, arr2):
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            j += 1
        i += 1
    
    return j == len(arr2)