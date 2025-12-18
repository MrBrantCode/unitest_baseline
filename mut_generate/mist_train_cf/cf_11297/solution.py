"""
QUESTION:
Implement a function `bubbleSortWithFlag(arr)` that sorts an input array `arr` using the bubble sort algorithm and returns the sorted array. The function should also include a flag to check if the array is already sorted, in which case it should return a message "Array already sorted." The function should modify the input array in-place and should not use any built-in sorting functions.
"""

def bubbleSortWithFlag(arr):
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
    if sorted:
        return "Array already sorted."
    else:
        return arr