"""
QUESTION:
Implement the `selection_sort` function, which sorts an array of integers in ascending order using the selection sort algorithm. The function takes one parameter, `arr`, representing the input array, and returns the sorted array.
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr