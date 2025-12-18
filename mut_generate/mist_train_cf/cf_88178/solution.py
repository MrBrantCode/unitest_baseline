"""
QUESTION:
Write a stable sorting function `bubble_sort(arr)` that sorts the input list in ascending order, has a time complexity of O(n^2) or less, and a space complexity of O(n) or less. The input list can contain duplicate elements and the relative order of equal elements should be preserved.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr