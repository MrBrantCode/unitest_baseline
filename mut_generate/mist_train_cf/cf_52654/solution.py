"""
QUESTION:
Implement a function named `mySort` that takes an array of integers as input, sorts it using the Bubble Sort algorithm, and returns the sorted array along with the total number of swaps made during the sorting process. The function should be optimized to stop early if the input array is already sorted.
"""

def mySort(arr):
    n = len(arr)
    swap_count = 0

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
                swapped = True
        # If no two elements were swapped by inner loop, then the list is sorted. 
        if not swapped:
            break
    return arr, swap_count