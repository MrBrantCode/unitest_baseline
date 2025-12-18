"""
QUESTION:
Write a function called `smallest_prime` that takes a list of integers as input and returns the smallest prime number in the list. The function should return `None` if there are no prime numbers in the list.
"""

def smallest_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while (i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i += 6
        return True

    primes = [num for num in numbers if is_prime(num)]
    return min(primes) if primes else None