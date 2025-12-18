"""
QUESTION:
Implement a function named `insertion_sort_descending` that sorts an array in descending order using the insertion sort algorithm. The function should take a list of integers as input and return the sorted list.
"""

def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        position = i

        while position > 0 and arr[position - 1] < current:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current
    return arr