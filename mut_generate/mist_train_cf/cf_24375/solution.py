"""
QUESTION:
Write a function named `find_primes_between` that takes two integers `n1` and `n2` as input and returns a list of prime numbers between `n1` and `n2` (inclusive). The function should be as concise as possible.
"""

def find_primes_between(n1, n2):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in range(n1, n2 + 1) if is_prime(num)]