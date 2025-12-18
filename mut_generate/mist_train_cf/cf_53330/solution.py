"""
QUESTION:
Write a function `find_pair(arr1, arr2, target)` that finds a pair of elements from two lists `arr1` and `arr2` that sum up to the `target` integer. The function should return the indices of the pair from their respective arrays. If there are multiple pairs that meet the condition, return the pair with the smallest non-negative integer index. If no such pair exists, return None. The function should have a time complexity lower than O(n^2).
"""

def find_pair(arr1, arr2, target):
    map = {}
    for i in range(len(arr1)):
        complement = target - arr1[i]
        map[complement] = i
    for j in range(len(arr2)):
        if arr2[j] in map:
            return [map[arr2[j]], j]
    return None