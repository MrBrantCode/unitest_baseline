"""
QUESTION:
Write a function `find_divisors(n)` that takes an integer `n` as input and returns a list of all divisors of `n` in descending order. The function should handle cases where `n` is negative or zero, and return an empty list if `n` is zero.
"""

def find_divisors(n):
    if n == 0:
        return []
    divisors = []
    for i in range(1, abs(n)+1):
        if n % i == 0:
            divisors.append(i)
    divisors.reverse()
    return divisors