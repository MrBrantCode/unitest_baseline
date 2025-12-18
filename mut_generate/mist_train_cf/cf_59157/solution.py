"""
QUESTION:
Write a function `get_positive_and_sort` that takes a list of integers as input, extracts the unique positive integers from the list, sorts them in ascending order, and returns them as a list. 

Create a helper function `swap_elements` that swaps two elements in a list. The `get_positive_and_sort` function should not use the built-in `sort()` or `sorted()` functions in Python. Instead, implement a custom sorting algorithm using the `swap_elements` helper function.
"""

def get_positive_and_sort(lst: list):
    """
    Function to fetch positive numbers and sort them in ascending order.
    Also, it removes all duplicates and returns only unique positive numbers.
    """
    def swap_elements(n: list, index1: int, index2: int):
        """Helper function for swapping elements"""
        n[index1], n[index2] = n[index2], n[index1]
        return n

    # Extract unique positive integers from the list
    unique_positive_integers = list(set([num for num in lst if num > 0]))

    # Implement Bubble Sort using the swap_elements helper function
    for i in range(len(unique_positive_integers)):
        for j in range(len(unique_positive_integers) - 1):
            if unique_positive_integers[j] > unique_positive_integers[j + 1]:
                unique_positive_integers = swap_elements(unique_positive_integers, j, j + 1)

    return unique_positive_integers