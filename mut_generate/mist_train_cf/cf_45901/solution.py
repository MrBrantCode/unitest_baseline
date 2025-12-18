"""
QUESTION:
Write a function `is_sum_prime(n)` that returns `True` if the input number `n` can be represented as the sum of five unique prime numbers and `False` otherwise. The input number `n` is less than 200.
"""

def is_sum_prime(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    primes = [i for i in range(2, n) if is_prime(i)]
    length = len(primes)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                for l in range(k + 1, length):
                    for m in range(l + 1, length):
                        if primes[i] + primes[j] + primes[k] + primes[l] + primes[m] == n:
                            return True
    return False