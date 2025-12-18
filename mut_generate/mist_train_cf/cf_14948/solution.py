"""
QUESTION:
Write a function `contains_only_primes` that checks if a given string of space-separated integers contains only prime numbers.
"""

def contains_only_primes(string):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    numbers = string.split()
    for number in numbers:
        if not is_prime(int(number)):
            return False
    return True