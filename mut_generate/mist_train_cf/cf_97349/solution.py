"""
QUESTION:
Write a function `find_second_smallest_prime` that takes a list of integers as input and returns the second smallest prime number in the list. The function should return `None` if the list contains less than two prime numbers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_second_smallest_prime(numbers):
    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes[1] if len(primes) > 1 else None