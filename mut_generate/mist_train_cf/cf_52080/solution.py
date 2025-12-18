"""
QUESTION:
Write a function `search_element` that takes a list of integers and a target integer as input, and returns `True` if the target is found in the list and `False` otherwise. Use a `for` loop with an `else` clause to achieve this. The function should not use any built-in functions like `in` or `index` to check for the presence of the target in the list.
"""

def search_element(lst, target):
    """
    Searches for a target integer in a list of integers using a for loop with an else clause.

    Args:
        lst (list): A list of integers.
        target (int): The target integer to search for.

    Returns:
        bool: True if the target is found in the list, False otherwise.
    """
    for num in lst:
        if num == target:
            return True
    else:
        return False