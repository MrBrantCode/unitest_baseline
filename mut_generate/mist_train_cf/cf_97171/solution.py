"""
QUESTION:
Implement a function named `bubble_sort` that sorts an array of integers in ascending order. The function should have a time complexity of O(n^2) and space complexity of O(1), where n is the number of elements in the array. The array will contain at most 1000 elements. The function should sort the array in place and return the sorted array.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr