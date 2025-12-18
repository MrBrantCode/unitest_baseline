"""
QUESTION:
Write a function `get_common_divisors` that calculates the number of positive integers that are common divisors of two numbers and can be expressed as the product of their prime factors. The function should take two integers as input and return the count of such divisors.
"""

def get_common_divisors(a, b):
    def get_prime_factors(n):
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


    def get_divisors(n):
        factors = get_prime_factors(n)
        divisors = set(factors)
        for i in range(len(factors)):
            for j in range(i+1, len(factors)):
                divisors.add(factors[i]*factors[j])
        divisors.add(n)
        return divisors


    divisors_a = get_divisors(a)
    divisors_b = get_divisors(b)

    common_divisors = divisors_a.intersection(divisors_b)

    return len(common_divisors)