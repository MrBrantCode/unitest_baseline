"""
QUESTION:
Implement a function `bubble_sort_descending` that sorts an array of positive integers in descending order using the Bubble Sort Algorithm. The function should handle edge cases such as an empty array or an array with duplicate elements, minimize unnecessary swaps, and return the sorted array along with the number of swaps performed.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    swaps = 0

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return arr, swaps