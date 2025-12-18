"""
QUESTION:
Write a function, `filter_numbers`, that takes a list of integers and a predicate as input, filters the list based on the predicate, and returns a new list containing only the filtered numbers in ascending order. The predicate should return True for numbers that are divisible by 3 and False for all other numbers.
"""

def filter_numbers(numbers, predicate):
    """
    This function filters a list of integers based on a given predicate and returns 
    a new list containing only the filtered numbers in ascending order.

    Args:
        numbers (list): A list of integers to be filtered.
        predicate (function): A function that takes an integer and returns a boolean.

    Returns:
        list: A new list containing the filtered numbers in ascending order.
    """
    filtered_numbers = list(filter(predicate, numbers))
    filtered_numbers.sort()
    return filtered_numbers