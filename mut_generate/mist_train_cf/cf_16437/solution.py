"""
QUESTION:
Create a function named `get_primes` that takes an integer `n` as input and returns the first `n` prime numbers in reverse order. The function should not take any other arguments.
"""

def get_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return sorted(primes, reverse=True)