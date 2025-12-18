"""
QUESTION:
Function name: sum_of_primes_in_range

Write a function sum_of_primes_in_range that takes a range of two integers and returns the sum of all prime numbers in that range. The range is inclusive. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def sum_of_primes_in_range(a, b):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(num for num in range(a, b + 1) if is_prime(num))