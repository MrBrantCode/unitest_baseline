"""
QUESTION:
Write a function called `add_numbers` that takes two arguments and returns their sum. The function should handle positive and negative integers, floating point numbers, and zero as inputs, and it should correctly handle edge cases such as very large or very small numbers. The function should also handle non-numeric inputs by returning an error message. The function should be efficient enough to handle large inputs and a large number of inputs.
"""

def add_numbers(a, b):
    """
    This function takes two arguments and returns their sum.
    It handles positive and negative integers, floating point numbers, and zero as inputs.
    It correctly handles edge cases such as very large or very small numbers.
    It also handles non-numeric inputs by returning an error message.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b, or an error message if either input is non-numeric.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Non-numeric input"
    return a + b