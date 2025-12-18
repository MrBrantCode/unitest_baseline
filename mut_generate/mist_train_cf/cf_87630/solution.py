"""
QUESTION:
Implement the `bubble_sort_descending` function that sorts an array in descending order using the bubble sort algorithm with a time complexity of O(n^2) and a space complexity of O(1). The function should take an array of integers as input and return the sorted array.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr