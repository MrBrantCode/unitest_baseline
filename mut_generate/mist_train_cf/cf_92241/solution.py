"""
QUESTION:
Create a function named `check_number_in_array` that takes two parameters: a list of integers and a target integer. The function should return a boolean value indicating whether the target integer exists in the list and its index position if it exists. If the target integer does not exist, the function should return False and -1 as the index position.
"""

def check_number_in_array(numbers, target):
    """
    Checks if a target integer exists in a list of integers and returns its index position.

    Args:
        numbers (list): A list of integers.
        target (int): The target integer to search for.

    Returns:
        tuple: A boolean indicating whether the target integer exists and its index position if it exists, otherwise -1.
    """
    for index, number in enumerate(numbers):
        if number == target:
            return True, index
    return False, -1