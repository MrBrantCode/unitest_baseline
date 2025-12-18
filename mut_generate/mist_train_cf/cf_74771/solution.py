"""
QUESTION:
Create a function `get_positive_and_sort` that takes a list of integers as input and returns a new list containing only the positive numbers from the original list, sorted in ascending order. Implement a custom sorting algorithm in a separate helper function called `swap_elements` without using the built-in `sort()` or `sorted()` functions. The function `swap_elements` should swap two elements in the list. The main function `get_positive_and_sort` should filter out non-positive numbers and then sort the remaining numbers using the `swap_elements` function.
"""

def get_positive_and_sort(lst: list):
    # Filter the positive numbers
    lst = [num for num in lst if num > 0]

    def swap_elements(n: list, index1: int, index2: int):
        # Implement a helper function for sorting elements
        n[index1], n[index2] = n[index2], n[index1]

    # Implement a custom sorting algorithm
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                swap_elements(lst, j, j+1)

    return lst