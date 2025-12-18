"""
QUESTION:
Implement a function named `selection_sort` that sorts an array in ascending order using the selection sort algorithm. The function should have one parameter, `arr`, representing the input array. Assume the input array contains distinct elements and the function should return the sorted array.
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr