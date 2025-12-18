"""
QUESTION:
Design a function named `check_all_primes(numbers_set)` that takes a set of integers as input and returns `True` if all numbers in the set are prime numbers, and `False` otherwise. The function should consider 1 as a non-prime number.
"""

def check_all_primes(numbers_set):
    """This function checks if all numbers in a set are prime."""
    def is_prime(n):
        """This function returns True if the number is prime and False otherwise."""
        if n == 1 or (n % 2 == 0 and n > 2): 
            return False
        for divisor in range(3, int(n**0.5) + 1, 2):
            if n % divisor == 0:
                return False
        return True

    for num in numbers_set:
        if not is_prime(num):
            return False
    return True