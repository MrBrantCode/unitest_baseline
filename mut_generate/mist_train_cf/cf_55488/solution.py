"""
QUESTION:
Implement the `selectionSort` function to sort an array of integers in ascending order using the selection sort algorithm, and return the sorted array. The input array is not guaranteed to be of a specific length, and the function should work for any array size.
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr