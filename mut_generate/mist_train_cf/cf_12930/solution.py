"""
QUESTION:
Implement a function `bubble_sort_with_swaps` that takes an array of integers as input, sorts it in ascending order using a variation of the bubble sort algorithm, and returns a tuple containing the sorted array and the number of swaps performed during the sorting process. The function should terminate early if no swaps are made in a pass, indicating the array is already sorted.
"""

def bubble_sort_with_swaps(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return arr, swaps