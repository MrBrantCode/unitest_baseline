"""
QUESTION:
Given a positive integer `n`, write a function named `find_factors(n)` that returns a list of all unique factors of `n` in ascending order. The function should include both prime and composite factors without any repetitions.
"""

def find_factors(n):
    factors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)
    return sorted(list(factors))