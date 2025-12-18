"""
QUESTION:
Create a function `prod_signs(arr)` that takes an array of integers as input. The function should return the sum of absolute values of distinct integer values multiplied by the product of the signs of each distinct prime number in the array. If the array contains no prime numbers, return None. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The sign of a number can be 1, -1, or 0. Ensure to handle duplicate values.
"""

def is_prime(n):
    if n in (2, 3): return True
    if n == 1 or n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True    

def prod_signs(arr):
    primes = [x for x in arr if is_prime(abs(x))]
    if not primes: return None
    sums = sum(abs(p) * (1 if p > 0 else -1) for p in set(primes))
    return sums