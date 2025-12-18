"""
ORIGINAL QUESTION:
Write a function `find_prime_factors(num)` that finds all the prime factors of a given number `num`. The function should return a list of prime factors, and the input number `num` should be a positive integer.
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

    return factors