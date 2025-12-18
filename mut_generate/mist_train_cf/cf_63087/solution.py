"""
QUESTION:
Write a function `sum_of_primes(num)` that calculates the sum of all prime numbers less than the given number `num`. The function should return the sum of these prime numbers.
"""

def sum_of_primes(num):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sq = int(n**0.5) + 1
        for i in range(3, sq, 2):
            if n % i == 0:
                return False
        return True

    return sum(x for x in range(num) if is_prime(x))