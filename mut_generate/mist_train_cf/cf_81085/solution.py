"""
QUESTION:
Implement a function `decrement` that takes two parameters: a non-negative integer `start_number` and a non-zero integer `decrement_value`. The function should decrement `start_number` by `decrement_value` in each step, appending each intermediate value to a list until `start_number` reaches zero, and then return the list. Handle the edge cases where `start_number` is less than zero, `decrement_value` is zero, or `start_number` is less than `decrement_value`.
"""

def decrement(start_number, decrement_value):
    """
    This function decrements the start_number by decrement_value in each step, 
    appending each intermediate value to a list until start_number reaches zero, 
    and then return the list.

    Args:
    start_number (int): A non-negative integer.
    decrement_value (int): A non-zero integer.

    Returns:
    list: A list of intermediate values.
    """
    try:
        if start_number < 0: 
            return [] # return empty list if starting number is less than zero
        if decrement_value == 0: 
            return "Error: Decrement value cannot be zero" # return error message if decrement value is zero to avoid infinite loop
        numbers = []
        while start_number > 0:
            numbers.append(start_number)
            start_number -= decrement_value
        return numbers
    except Exception as e:
        return str(e)