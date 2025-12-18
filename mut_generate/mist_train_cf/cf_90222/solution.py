"""
QUESTION:
Create a function called 'sort_dataset' that takes a list of integers as input, sorts the list in ascending order, and returns the sorted list without modifying the original list. The function should be designed with immutability and pure functions in mind, ensuring it has no side effects and always produces the same output for the same input.
"""

def sort_dataset(dataset):
    """
    Sorts a list of integers in ascending order without modifying the original list.

    Args:
        dataset (list): A list of integers.

    Returns:
        list: A new list with the elements sorted in ascending order.
    """
    return sorted(dataset)