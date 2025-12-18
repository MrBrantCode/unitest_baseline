"""
QUESTION:
Write a function `sum_digits_prime_factors` that takes two integers `a` and `b` and returns the sum of the digits in their prime factors. The function should find the prime factors of `a` and `b`, concatenate them into a single list, and then calculate the sum of all the digits in the prime factors.
"""

def sum_digits_prime_factors(a, b):
    def prime_factors(n):
        factors = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    a_factors = prime_factors(a)
    b_factors = prime_factors(b)
    all_factors = a_factors + b_factors
    digit_sum = sum(int(digit) for factor in all_factors for digit in str(factor))
    return digit_sum