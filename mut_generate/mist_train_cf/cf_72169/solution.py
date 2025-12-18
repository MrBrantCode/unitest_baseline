"""
QUESTION:
Write a function named `process_nested_list` that takes a 2D list of integers as input and performs the following operations:
- For each integer, compute and print its cube.
- Keep a cumulative product of all integers and return it.
- Store all prime numbers found in the list and return them.

The function should handle potential exceptions and errors that may arise during the operations.
"""

def process_nested_list(nested_list):
    """
    This function processes a 2D list of integers by computing and printing the cube of each integer, 
    keeping a cumulative product of all integers, and storing all prime numbers found in the list.

    Args:
    nested_list (list): A 2D list of integers.

    Returns:
    tuple: A tuple containing the cumulative product and a list of prime numbers.
    """
    def is_prime(n):
        """Helper function to check if a number is prime."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    cumulative_product = 1
    prime_numbers = []

    for sublist in nested_list:
        for num in sublist:
            try:
                print(f'The cube of {num} is {num ** 3}')
                cumulative_product *= num
                if is_prime(num):
                    prime_numbers.append(num)
            except TypeError:
                print(f'Error! {num} cannot be processed.')

    return cumulative_product, prime_numbers