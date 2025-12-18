"""
QUESTION:
Build a function `get_positive_and_sort()` that receives a list of integers and returns all positive numbers from the list, sorted in ascending order, without using Python's built-in `sort()` and `sorted()` functions. Implement a sorting algorithm using an embedded function named `swap_elements()` within `get_positive_and_sort()` to swap elements during the sorting process. The function should handle edge cases such as returning an empty list when there are no positive numbers and handling negative numbers and zeros in the input list. The function should also be efficient for large lists, implying a requirement for optimized time and space complexity.
"""

def get_positive_and_sort(lst: list):
    """
    Returns only positive numbers from the list, sorted in ascending order.
    """
    
    def swap_elements(n: list, index1: int, index2: int):
        """Swap elements at two given indices in the list."""
        n[index1], n[index2] = n[index2], n[index1]
    
    # Filter out non-positive numbers
    positive_numbers = [num for num in lst if num > 0]
    
    # Implement Bubble Sort to sort the list of positive numbers
    for i in range(len(positive_numbers)):
        for j in range(len(positive_numbers) - 1):
            if positive_numbers[j] > positive_numbers[j + 1]:
                swap_elements(positive_numbers, j, j + 1)
    
    return positive_numbers