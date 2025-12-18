"""
QUESTION:
Write a function named `calculate_sum_of_digits` that takes an integer as input and returns the sum of its digits. The function should use a while loop to extract and add each digit to the total sum, without using any external libraries or built-in sum functions.
"""

def calculate_sum_of_digits(num):
    """
    Calculate the sum of digits of a given integer.

    Args:
        num (int): The input integer.

    Returns:
        int: The sum of digits of the input integer.
    """
    total = 0
    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10
    return total