"""
QUESTION:
Implement a function named `odd_even_sort` that takes an array of integers as input and returns the sorted array using the Odd-Even Sort algorithm. The function should be able to handle arrays of any length, arrays with duplicate elements, arrays containing negative numbers, and arrays containing floating-point numbers.
"""

def odd_even_sort(arr):
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
    return arr