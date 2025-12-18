"""
QUESTION:
Implement a function named `mergeSort` that takes an array of integers as input and returns the array sorted in ascending order. The function should use the merge sort algorithm and handle arrays of any length, including those with duplicate or negative values.
"""

def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
        Left = arr[:mid]
        Right = arr[mid:]
 
        mergeSort(Left)
        mergeSort(Right)
 
        i = j = k = 0
 
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1
 
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1
 
        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1
    return arr