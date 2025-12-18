"""
QUESTION:
Construct a function called `bubble_sort` that takes in an array of integers and returns the sorted array in increasing order using the bubble sort algorithm. Implement the bubble sort algorithm from scratch without using any built-in sorting functions or libraries. The function should handle cases where the array is empty or has only one element.
"""

def entance(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr