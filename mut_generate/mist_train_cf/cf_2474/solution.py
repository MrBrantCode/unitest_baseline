"""
QUESTION:
Write a function named `find_prime_factors(num)` that finds the prime factors of a given number `num` between 1000 and 10000 and returns them in ascending order.
"""

def find_prime_factors(num):
    factors = []
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num = num / divisor
        else:
            divisor += 1
    return sorted(factors)