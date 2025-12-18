"""
QUESTION:
Create a function `get_positive_and_sort` that takes a list of integers as input, filters out the unique positive integers, and returns them in ascending order without using the built-in `sort()` or `sorted()` functions in Python. The function should also include a secondary function `swap_elements` to aid in the sorting process.
"""

def get_positive_and_sort(lst: list):
    """Returns only unique positive numbers from the list, sorted in ascending order."""

    def swap_elements(n: list, index1: int, index2: int):
        """Swap the elements at index1 and index2 in list n."""
        n[index1], n[index2] = n[index2], n[index1]

    unique_positives = list(set([num for num in lst if num > 0]))
    
    for i in range(len(unique_positives) - 1):
        for j in range(len(unique_positives) - 1 - i):
            if unique_positives[j] > unique_positives[j + 1]:
                swap_elements(unique_positives, j, j + 1)
                
    return unique_positives