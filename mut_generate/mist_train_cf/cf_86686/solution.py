"""
QUESTION:
Implement the bubble sort algorithm using both the optimized and unoptimized versions. The function should take an array of integers as input and return the sorted array. The optimized version should include a check to terminate the algorithm early if no swaps are made during an iteration.
"""

def entrance(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr