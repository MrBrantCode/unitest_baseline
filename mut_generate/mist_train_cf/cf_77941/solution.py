"""
QUESTION:
Create a function `find_divisors_and_prime_factors(n)` that takes an integer `n` as input, returns a dictionary where keys are the unique divisors of `n` (excluding 1 and `n`) and values are their corresponding prime factors. Implement this function with optimal time and space complexity.
"""

def find_divisors_and_prime_factors(n):
    def prime_factors(div):
        i = 2
        factors = []
        while i * i <= div:
            if div % i:
                i += 1
            else:
                div //= i
                factors.append(i)
        if div > 1:
            factors.append(div)
        return factors

    i = 2
    factor_dict = {}
    while i <= n//2:
        if n % i:
            i += 1
            continue
        else:
            factor_dict[i] = prime_factors(i)
        i += 1
    return factor_dict