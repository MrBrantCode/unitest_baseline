"""
QUESTION:
Develop a function named `product_of_primes` that takes an integer `n` as input and returns the product of all prime numbers less than or equal to `n`. The function should handle integers greater than 1 and consider a prime number as a natural number greater than 1 that has only two positive divisors: 1 and the number itself.
"""

def product_of_primes(n):
    def is_prime(num):
        """Check if a number is prime."""
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while (i * i <= num):
            if (num % i == 0 or num % (i + 2) == 0):
                return False
            i += 6 
        return True

    """Find the product of prime numbers less than or equal to n."""
    product = 1
    for i in range(2, n + 1):
        if is_prime(i):
            product *= i
    return product