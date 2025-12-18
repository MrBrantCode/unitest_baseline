"""
QUESTION:
Write a function `filter_primes` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should not use any built-in prime number checking functions or libraries.
"""

def filter_primes(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]