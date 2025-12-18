"""
QUESTION:
Implement a function named `bubble_sort` that takes an array of integers as input, sorts it using the bubble sort algorithm, and returns the sorted array along with the total number of swaps performed during the sorting process. The function should have a time complexity of O(n^2), where n is the number of elements in the input array.
"""

def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                
    return arr, swaps