"""
QUESTION:
Implement the `selection_sort` function that sorts an array in ascending order using the selection sort algorithm. The function should take one parameter `arr` (the input array) and return the sorted array. The array should be sorted in-place, i.e., the original array should be modified. The function should not use any built-in sorting functions or methods.
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr