"""
QUESTION:
Write a function named `sum_even_divisible_by_four` that takes a list of integers as input and returns the total sum of all even numbers in the list that are divisible by 4. If no such numbers are found, the function should return -1.
"""

def sum_even_divisible_by_four(numbers):
    """
    This function calculates the total sum of all even numbers in the list that are divisible by 4.
    If no such numbers are found, the function returns -1.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The total sum of all even numbers that are divisible by 4, or -1 if no such numbers are found.
    """

    total_sum = 0
    found = False

    for number in numbers:
        if number % 2 == 0 and number % 4 == 0:
            total_sum += number
            found = True

    if found:
        return total_sum
    else:
        return -1