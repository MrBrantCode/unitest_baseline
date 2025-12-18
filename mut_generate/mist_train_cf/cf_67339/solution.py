"""
QUESTION:
Generate a function `print_multiplication_table(number)` that takes an integer `number` between 2 and 20 and prints a multiplication table for the given number along with its prime factors for each multiple from 1 to 10. The output format should be: `{multiplier} * {number} = {multiple} \tPrime Factors: {prime_factors}`. Ensure the function is optimized for time and space complexity.
"""

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def print_multiplication_table(number):
    for i in range(1, 11):
        multiple = i * number
        factors = prime_factors(multiple)
        print(f"{i} * {number} = {multiple} \tPrime Factors: {', '.join(map(str, factors))}")