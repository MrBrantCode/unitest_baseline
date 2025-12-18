"""
QUESTION:
Implement a function called `sort_increasing_order` that takes a list of integers as input and returns the list sorted in increasing order. The function must not use any built-in sorting functions or libraries.
"""

def sort_increasing_order(numbers):
    """
    Sorts a list of integers in increasing order using bubble sort.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: The input list sorted in increasing order.
    """
    n = len(numbers)
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        # Start looking at each item of the list one by one, comparing it with its adjacent value
        for j in range(n - i - 1):
            # If we find an element that is greater than the next element in the list
            if numbers[j] > numbers[j + 1]:
                # Swap them
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                # Set the flag to True so we'll loop again after this iteration
                swapped = True
        # If no two elements were swapped in the last iteration, the list is already sorted, and we can terminate
        if not swapped:
            break
    return numbers