"""
QUESTION:
Write a function named `generate_factorials` that takes a non-negative integer `n` as input and returns a list of factorial numbers from 1 to `n`. The input value for `n` can be up to 10^9, so the solution should be optimized to handle large inputs efficiently.
"""

def generate_factorials(n):
    prime = 10**9 + 7  # Large prime number
    factorials = [1] * (n + 1)

    # Calculate factorials modulo prime
    for i in range(2, n + 1):
        factorials[i] = (factorials[i - 1] * i) % prime

    return factorials