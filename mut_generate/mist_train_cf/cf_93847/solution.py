"""
QUESTION:
Write a function to generate a list of squares of all prime numbers from 0 to 1000. The function should use a helper function to check if a number is prime. The output should be a list of integers where each integer is the square of a prime number within the given range. 

Restrictions: The function should not include 0 and 1 as prime numbers.
"""

def generate_prime_squares(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes_squared = [num ** 2 for num in range(2, n + 1) if is_prime(num)]
    return primes_squared