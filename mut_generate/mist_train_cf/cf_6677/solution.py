"""
QUESTION:
Write a function `filter_tuples` that takes a list of tuples as input, removes the tuples that contain only prime numbers, and returns the filtered list. The function should be efficient enough to handle a list size of up to 10^6.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_tuples(tuple_list):
    """
    This function filters out tuples that contain only prime numbers from the input list.

    Args:
        tuple_list (list): A list of tuples.

    Returns:
        list: The filtered list of tuples.
    """
    return [tup for tup in tuple_list if not all(is_prime(num) for num in tup)]