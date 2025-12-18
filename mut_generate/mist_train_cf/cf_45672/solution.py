"""
QUESTION:
Write a function `find_factors(num)` that determines all distinct factors of a given integer `num`. The function should return a list of distinct factors in ascending order. The input `num` will be a positive integer, and the function should be optimized to handle large inputs efficiently.
"""

def find_factors(num):
    """
    This function determines all distinct factors of a given integer num.
    
    Parameters:
    num (int): A positive integer.
    
    Returns:
    list: A list of distinct factors in ascending order.
    """
    factors = set()

    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num//i)
    
    return sorted(factors)