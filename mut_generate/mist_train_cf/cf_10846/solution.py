"""
QUESTION:
Write a function called `generate_primes(start, end)` that takes two integers `start` and `end` as input and returns a list of all prime numbers in the range from `start` to `end` (inclusive). Assume that the input values are well-formed integers and `start` is less than or equal to `end`.
"""

def generate_primes(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes