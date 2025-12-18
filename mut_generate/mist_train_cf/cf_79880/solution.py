"""
QUESTION:
Design a function named `sort_numbers` that sorts a list of 100 random numbers in either ascending or descending order based on a user input. The function should take a list of numbers and a boolean input (True for ascending order, False for descending order) as arguments. The input list should include at least one negative number and one duplicate number, and the function should be able to handle these cases correctly.
"""

def sort_numbers(num_list, ascending):
    """
    Sorts a list of numbers in either ascending or descending order.

    Args:
        num_list (list): A list of numbers.
        ascending (bool): True for ascending order, False for descending order.

    Returns:
        list: The sorted list of numbers.
    """
    if ascending:
        num_list.sort()
    else:
        num_list.sort(reverse=True)
    return num_list