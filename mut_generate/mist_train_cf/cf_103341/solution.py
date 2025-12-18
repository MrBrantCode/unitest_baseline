"""
QUESTION:
Write a function `sum_of_prime_factors(n)` that calculates the sum of all prime factors of a given number `n`. The function should take an integer `n` as input and return the sum of its prime factors. The function should work for all positive integers.
"""

def sum_of_prime_factors(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors_sum = 0
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors_sum += i
    if n > 1:
        factors_sum += n
    return factors_sum