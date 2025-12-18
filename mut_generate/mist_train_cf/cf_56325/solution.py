"""
QUESTION:
Create a function `get_positive_and_sort` that takes a list of integers as input and returns a new list containing only the positive numbers from the original list, sorted in ascending order. The function should not use Python's built-in `sort()` or `sorted()` functions. Instead, it should use a custom sorting function. 

The function should include an auxiliary function `swap_elements` to swap two elements in the list. 

The input list can contain any number of integers, including negative numbers and zeros. The function should handle lists of any length, including empty lists. 

For example, `get_positive_and_sort([-1, 2, -4, 5, 6])` should return `[2, 5, 6]`, and `get_positive_and_sort([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])` should return `[1, 2, 3, 3, 5, 9, 123]`.
"""

def get_positive_and_sort(l: list):
    """Return only positive numbers and the digits should be sorted in ascending order."""

    def swap_elements(n: list, index1: int, index2: int):
        # A function to swap elements
        n[index1], n[index2] = n[index2], n[index1]

    positive_list = [num for num in l if num > 0]
    n = len(positive_list)
    
    # Implementing bubble sort
    for i in range(n):
        for j in range(0, n-i-1):
            if positive_list[j] > positive_list[j+1]:
                swap_elements(positive_list, j, j+1)

    return positive_list