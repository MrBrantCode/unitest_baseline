"""
QUESTION:
Write a function `get_positive_and_sort(lst)` that takes a list of integers as input and returns a new list containing only the positive integers from the original list, sorted in ascending order. The function should not modify the original list and should handle lists of any length.
"""

def get_positive_and_sort(lst: list):
    """Return only positive numbers from the list, sorted in ascending order."""
    
    def swap_elements(n: list, index1: int, index2: int):
        """Swap elements at index1 and index2"""
        n[index1], n[index2] = n[index2], n[index1]

    # Create a new list with only the positive integers from the original list
    positive_integers = [num for num in lst if num > 0]

    # Implement a simple bubble sort algorithm
    for i in range(len(positive_integers)):
        for j in range(len(positive_integers) -1):
            if positive_integers[j] > positive_integers[j + 1]:
                swap_elements(positive_integers, j, j + 1)

    return positive_integers