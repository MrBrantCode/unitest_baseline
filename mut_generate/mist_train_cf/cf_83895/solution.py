"""
QUESTION:
Create a function named `factorize` that takes an integer `n` as input and returns a list of tuples, where each tuple contains a distinct prime factor of `n` and its respective exponent. The list should be in ascending order of the prime factors and `n` should be equal to the product of all prime factors raised to their respective exponents. The time complexity should be no greater than O(sqrt(n)) and the space complexity should be no greater than O(log(n)).
"""

def factorize(n):
    """
    This function takes an integer n as input and returns a list of tuples, 
    where each tuple contains a distinct prime factor of n and its respective exponent.
    
    The list is in ascending order of the prime factors and n is equal to the product 
    of all prime factors raised to their respective exponents.
    
    The time complexity is O(sqrt(n)) and the space complexity is O(log(n)).
    
    Args:
        n (int): The input integer.
    
    Returns:
        list[tuple[int, int]]: A list of tuples containing prime factors and their exponents.
    """
    factors = []
    for i in range(2, int(n**0.5) + 1):
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            factors.append((i, count))
    if n > 1:
        factors.append((n, 1))
    return factors