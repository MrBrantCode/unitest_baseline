"""
QUESTION:
Find the smallest positive integer missing from a sorted array. The array can be sorted in either non-increasing or non-decreasing order and may contain negative numbers or zeros. The solution should have a time complexity of O(n) and a space complexity of O(1).
"""

def findSmallest(arr: list[int]) -> int:
    m = 1
    for i in range(len(arr)):
        if arr[i] > m:
            return m
        elif arr[i] > 0:
            m += arr[i]
    return m