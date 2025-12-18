"""
QUESTION:
Write a function called `sort_array_descending` that sorts the elements of a given array in descending order. The function should take an array of integers as input and return the sorted array. The function should be efficient and avoid unnecessary iterations or comparisons. The time complexity of the function should be optimized to minimize its running time.
"""

def sort_array_descending(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break
    return arr