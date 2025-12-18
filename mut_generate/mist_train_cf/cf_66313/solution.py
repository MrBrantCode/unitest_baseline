"""
QUESTION:
Create a function `LargestPrimeFactor(n: int)` that takes an integer `n` greater than 1 and not a prime number as input, and returns the maximum prime factor of `n`. The function should be efficient for large inputs.
"""

def largest_prime_factor(n: int) -> int:
    """
    This function calculates the maximum prime factor of a given number.

    Args:
    n (int): The input number.

    Returns:
    int: The maximum prime factor of n.
    """

    max_prime = -1
    while n % 2 == 0:
        max_prime = 2
        n >>= 1
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            max_prime = i
            n = n / i
    if n > 2:
        max_prime = n
    return int(max_prime)