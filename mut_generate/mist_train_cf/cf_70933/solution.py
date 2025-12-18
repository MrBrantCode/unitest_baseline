"""
QUESTION:
Create a function `search_prime_numbers(n)` that returns a list of all prime numbers up to `n`. The function should have an improved time complexity compared to the initial O(n^2) solution, and its time complexity should remain polynomial. The function should return an empty list if `n` is less than 2.
"""

def search_prime_numbers(n):
    if n < 2:
        return []

    primes = [2]
    for num in range(3, n + 1, 2):
        sqrtnum = int(num ** 0.5)
        for prime in primes:
            if prime > sqrtnum:
                primes.append(num)
                break
            if num % prime == 0:
                break
    return primes