"""
QUESTION:
Implement a function `bubble_sort(arr)` that sorts an array of integers in ascending order with a time complexity of O(n^2) and space complexity of O(1). The function should be able to handle arrays of up to 1000 elements and preserve the relative order of duplicate elements.
"""

def entrance(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr