"""
QUESTION:
Write a function named `find_max_min` that takes an array of integers as input. The function should find the maximum and minimum elements in the array, swap their positions, remove any duplicates, and sort the array in descending order. The function should return the modified array.
"""

def find_max_min(arr):
    max_val = float('-inf')
    min_val = float('inf')
    max_idx = -1
    min_idx = -1

    # Find maximum and minimum elements
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i

    # Swap positions of maximum and minimum elements
    arr[max_idx], arr[min_idx] = arr[min_idx], arr[max_idx]

    # Remove duplicates
    arr = list(set(arr))

    # Sort the array in descending order
    arr.sort(reverse=True)

    return arr