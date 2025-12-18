"""
QUESTION:
Create a function named `is_prime()` that generates prime numbers from 1 to n (inclusive) with a time complexity of O(n√n) without using any external libraries or built-in functions for prime number generation. The function should take an integer as input and return a list of all prime numbers in the given range.
"""

def is_prime(n):
    """Generates prime numbers from 1 to n (inclusive) with a time complexity of O(n√n)."""
    
    def check_prime(num):
        """Helper function to check if a number is prime."""
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False

        return True
    
    primes = []
    for num in range(1, n + 1):
        if check_prime(num):
            primes.append(num)
    
    return primes