"""
QUESTION:
Implement the quick_sort function to sort an unsorted array of integers using the quick sort algorithm with the Lomuto partition scheme. The function should handle arrays containing both positive and negative numbers, duplicate numbers, and edge cases such as empty arrays or arrays with one element. The output should be in ascending order. The function should not use any built-in sorting functions or libraries.
"""

def entrance(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # Select the last element as the pivot
    i = 0  # Index to track the position of the pivot

    for j in range(len(arr)-1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[-1] = arr[-1], arr[i]  # Move pivot to its correct position

    left = entrance(arr[:i])
    right = entrance(arr[i+1:])

    return left + [arr[i]] + right