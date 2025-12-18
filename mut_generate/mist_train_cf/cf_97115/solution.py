"""
QUESTION:
Implement a function named `insertion_sort_desc` that sorts an array of integers in descending order using the insertion sort algorithm. The array can contain duplicate elements, and the algorithm should have a time complexity of O(n^2).
"""

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr