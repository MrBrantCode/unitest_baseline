"""
QUESTION:
Implement the Odd-Even Sort algorithm as a function named `odd_even_sort` that takes an array of integers as input and returns the sorted array. The function should handle arrays of any length, arrays with duplicate elements, arrays containing negative numbers, and arrays containing floating-point numbers. The function should be efficient for large arrays.
"""

def odd_even_sort(arr):
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True
        # Perform odd-even comparison and swap
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        # Perform even-odd comparison and swap
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
    return arr