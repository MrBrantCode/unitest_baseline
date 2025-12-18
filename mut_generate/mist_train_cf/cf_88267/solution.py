"""
QUESTION:
Write a function called `sum_even_divisible_by_four` that calculates the total sum of all even numbers that are divisible by 4 in a given list. If there are no even numbers divisible by 4 in the list, return -1.
"""

def sum_even_divisible_by_four(numbers):
    """
    This function calculates the total sum of all even numbers that are divisible by 4 in a given list.
    If there are no even numbers divisible by 4 in the list, it returns -1.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The total sum of all even numbers that are divisible by 4, or -1 if not found.
    """

    total_sum = 0
    found = False

    for number in numbers:
        if number % 2 == 0 and number % 4 == 0:
            total_sum += number
            found = True

    return total_sum if found else -1