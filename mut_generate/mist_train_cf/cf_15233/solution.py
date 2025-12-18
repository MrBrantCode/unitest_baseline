"""
QUESTION:
Design a function `kth_smallest(arr, k)` that returns the k-th smallest element in the given array `arr` of integers. The array may contain duplicates and can have both positive and negative integers. The function must have a time complexity of O(nlogn) and space complexity of O(1), where n is the number of elements in the array.
"""

def kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]