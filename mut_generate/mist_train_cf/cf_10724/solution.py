"""
QUESTION:
Implement the `bubble_sort` function to sort an array of numbers in ascending order using a single loop and without using any built-in sorting functions or methods. The function should return the sorted array. The array is expected to contain only numbers.
"""

def bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False

        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr