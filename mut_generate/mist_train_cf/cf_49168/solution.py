"""
QUESTION:
Create a function `get_positive_and_sort` that takes a list of integers as input, filters out non-positive numbers, sorts the remaining positive numbers in ascending order, and returns them as a list. Implement a helper function `swap_elements` inside `get_positive_and_sort` to swap two elements in a list. The function should not use built-in sorting methods, instead, it should implement a sorting algorithm (like bubble sort).
"""

def get_positive_and_sort(numbers: list):
    """Return only positive numbers in the list, sorted in ascending order."""
    
    def swap_elements(lst: list, index1: int, index2: int):
        """Swap two elements in a list."""
        lst[index1], lst[index2] = lst[index2], lst[index1]

    # Collect only positive elements
    positive_numbers = [num for num in numbers if num > 0]
    
    # Sort the list using bubble sort method
    for i in range(len(positive_numbers) - 1):
        for j in range(len(positive_numbers) - 1 - i):
            if positive_numbers[j] > positive_numbers[j + 1]:
                swap_elements(positive_numbers, j, j + 1)
    
    return positive_numbers