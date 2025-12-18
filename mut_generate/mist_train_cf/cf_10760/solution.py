"""
QUESTION:
Find two numbers that are factors of the given number and sum up to the given number. The function should be named `find_factor_pair`. The given number is 12, but the function should be able to work with any number.
"""

def find_factor_pair(n):
    """
    This function finds two numbers that are factors of the given number and sum up to the given number.

    Args:
        n (int): The given number.

    Returns:
        tuple: A tuple containing two numbers that are factors of n and sum up to n. If no such pair is found, returns None.
    """
    for i in range(1, n):
        if n % i == 0 and i + (n // i) == n:
            return (i, n // i)
    return None