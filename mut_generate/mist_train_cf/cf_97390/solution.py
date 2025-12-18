"""
QUESTION:
Create a function named `filter_primes` that filters out all prime numbers from a given list of integers and returns the list of prime numbers. The list may contain negative numbers, but the function should treat them as their absolute values. Do not use any built-in functions or libraries to determine whether a number is prime.
"""

def filter_primes(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in numbers if is_prime(abs(num))]
    return primes