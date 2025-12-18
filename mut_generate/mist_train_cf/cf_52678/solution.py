"""
QUESTION:
Write a function named `peakIndexInMountainArray` that takes a mountain array `arr` as input and returns any index `i` that satisfies the mountain array conditions. The array length is between 3 and 10^4 (inclusive), and each element is between 0 and 10^6 (inclusive). The array is guaranteed to be a mountain array. The function should have a time complexity of O(log(n)).
"""

def peakIndexInMountainArray(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return right