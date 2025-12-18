"""
QUESTION:
Implement the `bubble_sort_descending` function, which takes a list of numbers as input and returns the sorted list in descending order. The function should utilize the bubble sort algorithm and handle duplicate numbers by maintaining their original order relative to other duplicate numbers. The function should be able to handle lists of any length.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr