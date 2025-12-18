"""
QUESTION:
Write a function `get_first_n_primes(n)` that returns the first n prime numbers. The function should have a time complexity of O(n^2) or better.
"""

def entrance(n):
    primes = []
    num = 2
    while len(primes) < n:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
        num += 1
    return primes