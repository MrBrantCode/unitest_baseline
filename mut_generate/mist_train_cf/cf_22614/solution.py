"""
QUESTION:
Implement a function named `bubble_sort` that sorts an array of integers in ascending order using the Bubble Sort algorithm with a time complexity of O(n^2) and space complexity of O(1). The function should take one argument, `arr`, which is a list of integers, and return the sorted array. The length of the input array will not exceed 1000 elements.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr