"""
QUESTION:
Implement a function `bubble_sort_descending(arr)` that sorts an array of numbers in descending order using the bubble sort algorithm. The array may contain duplicates, which should be grouped together, and negative numbers should be placed before positive numbers. The function should work with arrays containing both integers and floating-point numbers.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr