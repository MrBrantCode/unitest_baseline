"""
QUESTION:
Write a function named `factorize` that takes an integer `n` as input, where `2 ≤ n ≤ 10^6`, and returns a tuple containing a sorted list of prime factors and a dictionary with prime factors as keys and their occurrence counts as values. The list should be sorted based on the frequency of the prime factors in the factorization, and the input number should be equal to the product of all factors.
"""

from typing import List, Tuple, Dict
from collections import defaultdict

def factorize(n: int) -> Tuple[List[int], Dict[int, int]]:
    """
    This function takes an integer n as input, where 2 ≤ n ≤ 10^6, 
    and returns a tuple containing a sorted list of prime factors and 
    a dictionary with prime factors as keys and their occurrence counts as values.

    Args:
        n (int): The number to be factorized.

    Returns:
        Tuple[List[int], Dict[int, int]]: A tuple containing a sorted list of prime factors 
        and a dictionary with prime factors as keys and their occurrence counts as values.
    """
    factor_count = defaultdict(int)
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factor_count[i] += 1
    if n > 1:
        factor_count[n] += 1
    
    # Sort factors based on their counts in descending order and then by their values in ascending order
    sorted_factors = sorted(factor_count, key=lambda x: (-factor_count[x], x))
    
    return sorted_factors, dict(factor_count)