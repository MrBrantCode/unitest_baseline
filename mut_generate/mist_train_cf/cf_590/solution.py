"""
QUESTION:
Write a function called `generate_unique_prime` that takes two integers, `start` and `end`, representing a range of numbers. The function should return a unique prime number within this range that is not divisible by any previously generated prime numbers. If no such prime number exists, return `None`.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_unique_prime(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            if all(num % prime != 0 for prime in primes):
                primes.append(num)
                return num
    return None