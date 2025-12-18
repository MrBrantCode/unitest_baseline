"""
QUESTION:
Write a function called `is_prime` that takes an integer `number` as input and returns a boolean value indicating whether the number is prime or not. The function must use a boolean variable within a loop structure to solve the problem.
"""

def is_prime(number):
    """
    Checks if a given number is prime or not.

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    return is_prime