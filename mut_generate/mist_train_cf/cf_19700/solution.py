"""
QUESTION:
Write a function named `custom_sort_descending` that takes a list of numbers as input and sorts them in descending order using a custom sorting algorithm. The function should check if the input list is already sorted in descending order, and if so, return the list as is. If not, the function should sort the list using the custom sorting algorithm. The function should also handle cases where the input list contains non-numeric values.
"""

def custom_sort_descending(numbers):
    """
    This function takes a list of numbers as input, checks if it's already sorted in descending order,
    and if not, sorts it using a custom bubble sort algorithm.

    Args:
        numbers (list): A list of numbers

    Returns:
        list: The sorted list of numbers in descending order
    """

    # Check if the list is already sorted in descending order
    for i in range(len(numbers)-1):
        if numbers[i] < numbers[i+1]:
            # Perform custom sorting in descending order using bubble sort algorithm
            n = len(numbers)
            for i in range(n-1):
                for j in range(n-1-i):
                    if numbers[j] < numbers[j+1]:
                        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            return numbers
    return numbers