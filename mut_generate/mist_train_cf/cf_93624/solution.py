"""
QUESTION:
Write a function `compute_max_values` that takes a dictionary as input, where each value is an integer. The function should return a new dictionary containing the maximum value for each key, but only if the value is divisible by 3 and has a prime number in its prime factorization. If no such value exists for a key, it should not be included in the output dictionary.
"""

def compute_max_values(d):
    max_values = {}
    for key, value in d.items():
        if isinstance(value, int) and value % 3 == 0 and has_prime_factor(value):
            if key not in max_values or value > max_values[key]:
                max_values[key] = value
    return max_values

def has_prime_factor(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 2
    if n != 1:
        factors.append(n)
    return any(is_prime(f) for f in factors)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True