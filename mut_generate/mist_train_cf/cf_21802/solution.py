"""
QUESTION:
Implement a function `insertion_sort(arr)` that sorts an array of integers in ascending order. The input array can contain duplicate values and may have up to 10^6 elements. The implementation should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr