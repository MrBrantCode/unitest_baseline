"""
QUESTION:
Create a function `decompose_and_calculate_sum(num)` that takes a positive integer greater than 1 as input and returns the prime factors of the number along with their sum. The function should decompose the input number into its prime factors and calculate the sum of these prime factors.
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