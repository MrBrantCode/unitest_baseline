"""
QUESTION:
Write a function `generate_primes(n)` that generates a list of prime numbers up to a given number `n`. The function should be optimized to handle large inputs efficiently and include error handling for non-integer or negative inputs. The function should return a list of prime numbers up to but not including `n`.
"""

def generate_primes(n):
    try:
        n = int(n)
        assert n >= 0
    except ValueError:
        return "Error: The input must be an integer."
    except AssertionError:
        return "Error: The input must be a non-negative integer."

    primes = [True for _ in range(n+1)]
    p = 2
    while p ** 2 <= n:
        if primes[p] is True:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers