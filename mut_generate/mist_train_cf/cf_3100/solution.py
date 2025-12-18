"""
QUESTION:
Write a function `sort_numbers(arr)` that sorts the given array of numbers from least to greatest, with even numbers before odd numbers. The function should sort the numbers in-place, without using any built-in sorting functions or additional data structures, and have a time complexity less than O(n^2). If the array is empty or contains only one element, return the array as it is.
"""

def sort_numbers(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if (arr[j] % 2 != 0 and arr[j+1] % 2 == 0) or (arr[j] % 2 == arr[j+1] % 2 and arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr