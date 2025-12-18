"""
QUESTION:
Implement the function bubble_sort(arr) to arrange the elements of the array in ascending order without using any built-in sorting functions. The array may contain duplicate elements. The time complexity of the solution should be as efficient as possible, and the space complexity should be O(1) with a maximum of two loops.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swaps are made in this pass
        swapped = False
        for j in range(0, n-i-1):
            # Swap if the current element is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps are made, the array is already sorted
        if not swapped:
            break
    return arr