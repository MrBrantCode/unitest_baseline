"""
QUESTION:
Implement a function `insertionSort(arr)` to sort an array of distinct integers in ascending order using the insertion sort algorithm. The function should take an array `arr` as input and return the sorted array.
"""

def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr