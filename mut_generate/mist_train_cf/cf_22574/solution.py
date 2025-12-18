"""
QUESTION:
Implement the "bubble_sort" function to sort an array of 10^5 elements in descending order using the bubble sort algorithm. The array will be sorted in-place, and the function should return the sorted array. The function should use a "swapped" variable to track if any swaps were made during a pass of the array, and repeat the process until no swaps are made during a pass.
"""

def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return arr