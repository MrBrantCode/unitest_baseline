"""
QUESTION:
Write a function named `bubble_sort` that sorts a list of numbers in ascending order using the bubble sort algorithm. The function should take a list of integers as input and return the sorted list. The function should have a time complexity of O(n^2).
"""

def bubble_sort(numbers):
    """
    Sorts a list of numbers in ascending order using the bubble sort algorithm.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: The sorted list of numbers.
    """
    n = len(numbers)
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False

        # Start looking at each item of the list one by one, comparing it with its adjacent value
        for j in range(n - i - 1):
            # If we come across an element that is greater than the next element, swap them
            if numbers[j] > numbers[j + 1]:
                # Swap values
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                # Set the flag to True so we'll loop again after this iteration
                swapped = True

        # If there were no swaps during the last iteration, the list is already sorted, and we can terminate
        if not swapped:
            break

    return numbers