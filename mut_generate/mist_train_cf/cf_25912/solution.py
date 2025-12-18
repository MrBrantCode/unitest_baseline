"""
QUESTION:
Write a function `get_primes` that takes a lower bound and an upper bound as input and returns a list of all prime numbers between the bounds (inclusive).
"""

def get_primes(lower, upper):
    """
    Returns a list of all prime numbers between the given lower and upper bounds (inclusive).
    
    Args:
    lower (int): The lower bound.
    upper (int): The upper bound.
    
    Returns:
    list: A list of prime numbers between the bounds.
    """
    primes = []
    for num in range(lower, upper + 1):
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes