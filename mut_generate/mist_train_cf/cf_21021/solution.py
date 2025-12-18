"""
QUESTION:
Create a function called `bubble_sort` that takes an array of numbers as input and returns the sorted array in ascending order. The function should have a time complexity of O(n^2) or better and a space complexity of O(1) or better. It should also be a stable sorting algorithm, preserving the relative order of equal elements.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr