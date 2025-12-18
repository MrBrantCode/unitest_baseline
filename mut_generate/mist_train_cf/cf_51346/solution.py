"""
QUESTION:
Create a Python function named `get_positive_and_sort` that takes a list of integers as input, filters out non-positive numbers, sorts the remaining numbers in ascending order using a custom sorting algorithm, and returns the sorted list. The custom sorting algorithm must be implemented in a separate auxiliary function named `bubble_sort` which in turn uses a helper function named `swap_elements` to swap elements. Do not use the built-in `sort()` or `sorted()` functions in Python.
"""

def get_positive_and_sort(l: list):
    def swap_elements(n: list, index1: int, index2: int):
        """Swap two elements in a list based on their indices."""
        n[index1], n[index2] = n[index2], n[index1]

    def bubble_sort(n: list):
        """Sort a list in place using the bubble sort algorithm."""
        for i in range(len(n)):
            for j in range(len(n) - 1):
                if n[j] > n[j + 1]:
                    swap_elements(n, j, j + 1)

    positive_nums = [num for num in l if num > 0]
    bubble_sort(positive_nums)
    return positive_nums