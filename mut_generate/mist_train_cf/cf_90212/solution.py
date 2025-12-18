"""
QUESTION:
Implement the `insertion_sort_desc` function to sort an array of integers in descending order using the insertion sort algorithm, with a time complexity of O(n^2), and without using any built-in sorting functions or libraries. The array can contain duplicate elements.
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