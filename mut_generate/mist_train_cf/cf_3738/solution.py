"""
QUESTION:
Write a function called `prime_factors` that takes an integer `n` as input and returns its prime factors. The function should be able to handle very large numbers efficiently, up to 10^15, with a time complexity less than O(sqrt(n) log(log(n))).
"""

def prime_factors(n):
    """
    Returns the prime factors of a given integer n.
    
    Parameters:
    n (int): The input integer to be factorized.
    
    Returns:
    list: A list of prime factors of n.
    """
    
    # Initialize an empty list to store prime factors
    factors = []
    
    # Handle edge cases where n is less than or equal to 1
    if n <= 1:
        return factors
    
    # Divide n by 2 until it's no longer divisible
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Find other prime factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors