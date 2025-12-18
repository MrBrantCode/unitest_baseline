"""
QUESTION:
Implement a function named `bubble_sort` that takes an array of integers as input, sorts it using the bubble sort algorithm, and returns the sorted array along with the total number of swaps made during the sorting process.
"""

def bubble_sort(arr):
    num_swaps = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            # swap elements if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                num_swaps += 1
    return arr, num_swaps