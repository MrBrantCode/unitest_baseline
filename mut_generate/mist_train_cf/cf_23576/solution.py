"""
QUESTION:
Implement a function named `selection_sort` that sorts an array in ascending order using the selection sort algorithm. The function should take an array of integers as input and return the sorted array. The array can contain any number of elements, and the elements can be in any order. The function should modify the input array in-place.
"""

def selection_sort(arr):
    for i in range(len(arr) - 1): 
        min = i 
        for j in range(i+1, len(arr)): 
            if arr[j] < arr[min]: 
                min = j 
        arr[i], arr[min] = arr[min], arr[i]
    return arr