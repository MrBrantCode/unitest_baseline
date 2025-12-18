"""
QUESTION:
Write a function `sum_primes(n)` that calculates the sum of all prime numbers from 1 to a given number `n` (inclusive) with a time complexity of O(n^2) and a space complexity of O(n).
"""

def sum_primes(n):
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return sum(primes)