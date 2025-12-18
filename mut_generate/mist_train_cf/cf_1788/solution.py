"""
QUESTION:
Write a function `product_of_primes(n)` that generates a list of prime numbers up to `n`, in descending order, and returns the product of all prime numbers in the list. The function `product_of_primes(n)` should take an integer `n` as input and return the product of all prime numbers up to `n`.
"""

def product_of_primes(n):
    """
    Generates a list of prime numbers up to n, in descending order, 
    and returns the product of all prime numbers in the list.

    Args:
    n (int): The upper limit for generating prime numbers.

    Returns:
    int: The product of all prime numbers up to n.
    """
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Generate a list of prime numbers up to n in descending order
    primes = [i for i in range(n, 1, -1) if is_prime(i)]

    # Return the product of all prime numbers
    product = 1
    for prime in primes:
        product *= prime
    return product