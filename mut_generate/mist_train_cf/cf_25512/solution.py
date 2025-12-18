"""
QUESTION:
Implement the `sorting_algorithm` function to sort an array of integers in ascending order. The function should take one argument, `arr`, which is a list of integers. Return the sorted list.
"""

def sorting_algorithm(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr