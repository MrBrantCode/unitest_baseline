"""
QUESTION:
Develop a function `min_max_values(lst)` that takes a list of integers as input and returns the smallest, largest, second smallest, and second largest values without using built-in functions like `sort()`, `max()`, or `min()`. The function should handle the edge case when the list contains less than 2 unique numbers, returning a message indicating insufficient unique elements.
"""

def min_max_values(lst):
    """
    This function takes a list of integers as input and returns the smallest, 
    largest, second smallest, and second largest values without using built-in 
    functions like `sort()`, `max()`, or `min()`.

    Args:
        lst (list): A list of integers.

    Returns:
        tuple: A tuple containing the smallest, largest, second smallest, and 
        second largest values. If the list contains less than 2 unique numbers, 
        it returns a message indicating insufficient unique elements.
    """

    smallest = None
    largest = None
    second_smallest = None
    second_largest = None

    if lst is None or len(lst) < 1:
        return "List is empty"

    for num in lst:
        if smallest is None:
            smallest = num
            largest = num
        else:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif second_smallest is None or second_smallest > num > smallest:
                second_smallest = num
            if num > largest:
                second_largest = largest
                largest = num
            elif second_largest is None or second_largest < num < largest:
                second_largest = num

    if smallest is None or largest is None or second_smallest is None or second_largest is None:
        return "Insufficient unique elements."
    else:
        return smallest, largest, second_smallest, second_largest