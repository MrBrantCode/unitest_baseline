"""
QUESTION:
Define a function `prod_signs(arr)` that takes an array of integers as input and returns the sum of the magnitudes of unique integers multiplied by the product of the signs of each distinct non-repeating prime number in the array, represented by 1, -1, or 0. The function should consider non-zero numbers only, ignore duplicates, and return None for an array with no prime numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sign(n):
    return n and (1, -1)[n < 0]

def prod_signs(arr):
    unique_primes = set()
    for i in arr:
        if is_prime(abs(i)):
            unique_primes.add(i)
    if not unique_primes:
        return None
    summed_magnitudes = sum(abs(x) for x in unique_primes)
    multiplied_signs = sign(sum(sign(x) for x in unique_primes))
    return summed_magnitudes * multiplied_signs