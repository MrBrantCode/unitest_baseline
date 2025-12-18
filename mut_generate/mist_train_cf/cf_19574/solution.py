"""
QUESTION:
Create a function `sum_of_cubes_of_primes(n)` that calculates the sum of the cubes of all prime numbers up to the given number `n`.
"""

def sum_of_cubes_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    sum_of_cubes = 0
    for num in range(2, n + 1):
        if is_prime(num):
            sum_of_cubes += num ** 3
    return sum_of_cubes