"""
QUESTION:
Create a function named is_prime_and_largest_prime_factor(n) that checks if a given integer n is prime and returns its largest prime factor. The function should return a tuple of form (is_prime, largest_prime_factor), where is_prime is a boolean indicating if n is prime and largest_prime_factor is the largest prime factor of n. If n is prime, is_prime should be True and largest_prime_factor should be n itself. The function should handle integers greater than 1.
"""

def entrance(n):
    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
    prime = is_prime(n)
    if not prime and n > 1:
        factor = 2
        while factor * factor <= n:
            if n % factor:
                factor += 1
            else:
                n //= factor
    return (prime, n)