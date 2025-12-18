"""
QUESTION:
Implement the `get_positive_and_sort` function to filter out all positive numbers from the given list, sort them in ascending order, and return the result. The function must not use the built-in `sort()` and `sorted()` functions. Instead, it should utilize a helper function `swap_elements` to swap elements in place for sorting purposes. The input list may contain both positive and negative integers, as well as zeros.
"""

def get_positive_and_sort(lst: list):
    """Returns only positive numbers from the list, sorted in ascending order."""

    def swap_elements(n: list, index1: int, index2: int):
        """Helper function to swap elements in place for sorting purposes."""
        n[index1], n[index2] = n[index2], n[index1]

    positive_list = [num for num in lst if num > 0]

    # Bubble sort algorithm
    for i in range(len(positive_list)):
        for j in range(len(positive_list) - 1):
            if positive_list[j] > positive_list[j + 1]:
                swap_elements(positive_list, j, j + 1)

    return positive_list