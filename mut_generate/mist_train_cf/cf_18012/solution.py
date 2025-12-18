"""
QUESTION:
Write a function `bubble_sort` that takes an array of integers as input and sorts the array in ascending order using the bubble sort algorithm. The function should also return the number of swaps performed during the sorting process.
"""

def bubble_sort(arr):
    n = len(arr)
    swaps = 0

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1

    return swaps