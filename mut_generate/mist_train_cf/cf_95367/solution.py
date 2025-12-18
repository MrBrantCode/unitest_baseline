"""
QUESTION:
Write a function called bubble_sort that sorts a list of integers in ascending order. The function should take one argument, arr, which is a list of integers. The function should return the sorted list. The function should optimize the bubble sort algorithm by stopping the iteration if no swaps are made in a pass, which means the list is already sorted.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr