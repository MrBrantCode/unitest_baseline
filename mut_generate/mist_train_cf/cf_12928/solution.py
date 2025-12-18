"""
QUESTION:
Implement a function `bubble_sort` that takes an array of integers as input and returns the array sorted in ascending order without using any built-in sorting functions or libraries. The input array can contain duplicate elements and may have a length of up to 10^6. The implementation should have a time complexity of O(n^2), where n is the length of the input array.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr