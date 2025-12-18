"""
QUESTION:
Create a function `primes_up_to_n(n)` to identify all prime numbers between 0 and `n`, where `n` can be a large number (up to 10^9). The function should have a time complexity of O(sqrt(n)) and return a list of prime numbers.
"""

def primes_up_to_n(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes