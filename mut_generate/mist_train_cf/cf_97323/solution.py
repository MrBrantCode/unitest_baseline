"""
QUESTION:
Write a function called `sum_of_cubes_of_primes` that takes an integer `n` as input and returns the sum of the cubes of the first `n` prime numbers. The function should return the sum as an integer. Note that the input `n` is a positive integer.
"""

def sum_of_cubes_of_primes(n):
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
    return sum([prime ** 3 for prime in primes])