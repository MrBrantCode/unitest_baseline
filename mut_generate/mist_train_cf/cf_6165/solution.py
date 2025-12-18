"""
QUESTION:
Write a function `lcm_n` that calculates the least common multiple of N numbers. The function should use prime factorization and have a time complexity of O(N log M), where M is the maximum value among the N numbers.
"""

def prime_factors(n):
    """Return a list of prime factors for a given number."""
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

def lcm_two_nums(a, b):
    """Return the least common multiple of two numbers."""
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)
    common_factors = set(factors_a) & set(factors_b)
    result = 1
    for factor in common_factors:
        result *= factor ** max(factors_a.count(factor), factors_b.count(factor))
    for factor in set(factors_a) ^ set(factors_b):
        result *= factor ** max(factors_a.count(factor), factors_b.count(factor))
    return result

def lcm_n(nums):
    """Return the least common multiple of N numbers."""
    lcm = nums[0]
    for num in nums[1:]:
        lcm = lcm_two_nums(lcm, num)
    return lcm