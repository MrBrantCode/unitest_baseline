"""
QUESTION:
Create a function named `decompose_and_calculate_sum` that takes a single integer `num` as input and returns the prime factors and their sum. The function should decompose the given number into its prime factors and calculate the sum of these prime factors. The input number is assumed to be a positive integer greater than 1.
"""

def decompose_and_calculate_sum(num):
    prime_factors = []
    divisor = 2

    while num > 1:
        if num % divisor == 0:
            prime_factors.append(divisor)
            num //= divisor
        else:
            divisor += 1

    prime_factor_sum = sum(prime_factors)

    return prime_factors, prime_factor_sum