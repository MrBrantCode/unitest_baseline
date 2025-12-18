"""
QUESTION:
Implement the `prime_factorization(n)` function to calculate the prime factors of a given number `n` and their corresponding exponents. The function should handle large input numbers efficiently with a time complexity of O(sqrt(n)). Additionally, implement the `prime_factors_array(numbers)` function to take an array of numbers and return an array of objects with each object containing the number and its prime factorization.
"""

def prime_factorization(n):
    factors = {}
    count = 0
    while n % 2 == 0:
        n = n / 2
        count += 1
    if count > 0:
        factors[2] = count

    factor = 3
    max_factor = round(n ** 0.5)
    while n > 1 and factor <= max_factor:
        count = 0
        while n % factor == 0:
            n = n / factor
            count += 1
        if count > 0:
            factors[factor] = count
        factor += 2
        max_factor = round(n ** 0.5)
 
    if n != 1: 
        factors[int(n)] = 1
    return factors