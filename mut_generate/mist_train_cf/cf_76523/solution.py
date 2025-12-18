"""
QUESTION:
Write a function `generate_primes(start, end)` that generates all prime numbers within a given range (inclusive). The function should return a list of prime numbers between `start` and `end`, including `start` and `end` if they are prime. Assume that `start` and `end` are integers and `start` is less than or equal to `end`.
"""

def generate_primes(start, end):
    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes