"""
QUESTION:
Write a function `generate_primes(n)` that generates the first `n` prime numbers. The function should take an integer `n` as input and return a list of the first `n` prime numbers. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes