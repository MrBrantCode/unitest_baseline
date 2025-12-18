"""
QUESTION:
Implement a function `bubble_sort(arr)` to sort an array of integers in ascending order, preserving the relative order of duplicate elements, with a time complexity of O(n^2) and a space complexity of O(1). The input array contains at most 1000 elements.
"""

def entance(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr