"""
QUESTION:
Write a function `get_combinations` that takes two lists `list1` and `list2` as input and returns a list of tuples containing all possible combinations of two elements, one from each list, with the following constraints:
- The first element in each tuple should be a prime number, an odd perfect square greater than 10, and less than 50.
- The second element in each tuple should be a multiple of 100, a power of 2, and less than 10000.
- The tuples should not contain any elements where the first and second elements are both divisible by 3.
- The tuples should be sorted first in descending order based on the product of their elements, and then in ascending order based on the difference between their elements.
- The length of each list should be at least 10.
- The tuples should not contain any duplicate elements.
"""

from itertools import product
from math import sqrt

def get_combinations(list1, list2):
    """
    Returns a list of tuples containing all possible combinations of two elements, 
    one from each list, with specific constraints.

    Args:
    list1 (list): A list of numbers.
    list2 (list): A list of numbers.

    Returns:
    list: A list of tuples.
    """
    # Filter list1 to include only prime numbers, odd perfect squares greater than 10, and less than 50
    list1 = [x for x in list1 if x % 2 != 0 and x > 10 and x < 50 and sqrt(x).is_integer() and is_prime(x)]
    
    # Filter list2 to include only multiples of 100, powers of 2, and less than 10000
    list2 = [x for x in list2 if x % 10 == 0 and x < 10000 and x % 2 == 0 and x % 3 != 0 and x % 100 == 0 and is_power_of_two(x)]
    
    # Generate all possible combinations of two elements, one from each list
    combinations = list(product(list1, list2))
    
    # Filter combinations to exclude tuples where both elements are divisible by 3
    combinations = [(x, y) for x, y in combinations if x % 3 != 0 or y % 3 != 0]
    
    # Sort combinations first in descending order based on the product of their elements, 
    # and then in ascending order based on the difference between their elements
    combinations = sorted(combinations, key=lambda x: (x[0] * x[1], abs(x[0] - x[1])), reverse=True)
    
    return combinations

def is_prime(n):
    """Check if number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(sqrt(n)) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def is_power_of_two(n):
    """Check if number is a power of two."""
    if n <= 0:
        return False
    return (n & (n - 1)) == 0