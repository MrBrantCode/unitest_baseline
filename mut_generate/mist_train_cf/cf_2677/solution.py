"""
QUESTION:
Write a recursive function `find_sum_and_product(n: int)` that calculates the sum of all even numbers and the product of all odd numbers between 0 and a given positive integer `n`. The function should return both the sum and the product as a tuple. The function should handle cases where `n` is zero or one, and it should not use any loops, built-in functions, or additional data structures.
"""

from typing import Tuple

def find_sum_and_product(n: int, curr_sum: int = 0, curr_product: int = 1) -> Tuple[int, int]:
    """
    This function calculates the sum of all even numbers and the product of all odd numbers between 0 and a given positive integer n.
    
    Args:
    n (int): A positive integer.
    curr_sum (int, optional): The current sum of even numbers. Defaults to 0.
    curr_product (int, optional): The current product of odd numbers. Defaults to 1.
    
    Returns:
    Tuple[int, int]: A tuple containing the sum of even numbers and the product of odd numbers.
    """
    
    # Base case: if n is 0, return the current sum and product
    if n == 0:
        return curr_sum, curr_product
    
    # Recursive case: if n is even, add it to the current sum
    if n % 2 == 0:
        curr_sum += n
    
    # Recursive case: if n is odd, multiply it with the current product
    else:
        curr_product *= n
    
    # Recursive call with n-1, updated sum, and updated product
    return find_sum_and_product(n-1, curr_sum, curr_product)