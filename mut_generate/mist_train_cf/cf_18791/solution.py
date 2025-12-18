"""
QUESTION:
Implement a correct and efficient version of the bubble sort algorithm, taking into account the limitations and potential errors in the provided incorrect implementation. Your function should be named `bubble_sort` and should sort the input list in ascending order.
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