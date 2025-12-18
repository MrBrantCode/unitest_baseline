"""
QUESTION:
Write a function called `calculate_even_sum` that takes a list of elements as input, calculates the sum of all even integers in the list, and returns the sum. The function should handle non-integer values in the list without terminating. The input list can contain a mix of integers and non-integer values.
"""

def calculate_even_sum(numbers):
    """
    Calculate the sum of all even integers in a list.

    Args:
    numbers (list): A list containing a mix of integers and non-integer values.

    Returns:
    int: The sum of all even integers in the list.
    """
    even_sum = 0
    for num in numbers:
        try:
            if isinstance(num, int) and num % 2 == 0:
                even_sum += num
        except TypeError:
            pass
    return even_sum