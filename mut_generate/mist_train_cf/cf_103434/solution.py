"""
QUESTION:
Write a function called `prime_sum_and_product` that takes a range defined by two integers `start` and `end` as input. The function should return a tuple containing the sum and product of all prime numbers within the given range (inclusive). The input range is guaranteed to be 1 <= start < end <= 100.
"""

def prime_sum_and_product(start, end):
    """
    This function calculates the sum and product of all prime numbers within a given range.
    
    Args:
    start (int): The start of the range (inclusive).
    end (int): The end of the range (inclusive).
    
    Returns:
    tuple: A tuple containing the sum and product of all prime numbers in the given range.
    """

    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Generate all prime numbers within the given range
    primes = [i for i in range(start, end + 1) if is_prime(i)]

    # Calculate the sum and product of prime numbers
    prime_sum = sum(primes)
    prime_product = 1
    for prime in primes:
        prime_product *= prime

    return prime_sum, prime_product