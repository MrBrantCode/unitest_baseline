"""
QUESTION:
Create a function `sort_array(arr)` that sorts a given array of integers in ascending order. The function should modify the input array in-place and return the sorted array. The array may contain duplicate values and the function should be able to handle it.
"""

def sort_array(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # swap
    return arr