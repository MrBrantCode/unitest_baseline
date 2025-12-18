"""
QUESTION:
Write a function named `find_primes` that takes two parameters, `n` and `m`, where `n` and `m` are positive integers and `n` is less than `m`. The function should return a list containing all prime numbers from `n` to `m`, not including `m`.
"""

def find_primes(n, m):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if n >= m:
        return []
    primes = [num for num in range(n, m) if is_prime(num)]
    return primes