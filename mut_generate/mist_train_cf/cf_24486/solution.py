"""
QUESTION:
Create a function called 'find_prime_factors' that takes an integer 'n' as input and returns a list of its prime factors. The function should identify all prime numbers that can evenly divide 'n' without leaving a remainder. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def find_prime_factors(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_factors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            prime_factors.append(i)
    return prime_factors