"""
QUESTION:
Write a function `mobius_error` that calculates the expected error `E(Δ|μ(k), n, m)` given the Möbius function `μ(k)`, the number of terms `n` in the product, and the length of the random sample `m`. The function should return the expected error rounded to six decimal places.

Restrictions: 
- `n` and `m` are positive integers.
- `1 ≤ m ≤ n`.
"""

def mobius_error(n, m):
    """
    Calculate the expected error E(Δ|μ(k), n, m) given the Möbius function μ(k), 
    the number of terms n in the product, and the length of the random sample m.

    Args:
        n (int): The number of terms in the product.
        m (int): The length of the random sample.

    Returns:
        float: The expected error rounded to six decimal places.
    """

    # Define a function to calculate the Möbius function μ(k)
    def mobius(k):
        if k == 1:
            return 1
        factors = prime_factors(k)
        if len(factors) != len(set(factors)):
            return 0
        return (-1) ** len(factors)

    # Define a function to calculate prime factors of a number
    def prime_factors(k):
        i = 2
        factors = []
        while i * i <= k:
            if k % i:
                i += 1
            else:
                k //= i
                factors.append(i)
        if k > 1:
            factors.append(k)
        return factors

    # Initialize variables to calculate the expected error
    total = 0
    for k in range(1, n + 1):
        total += mobius(k)

    # Calculate the expected error
    error = (1 - (m / n)) ** abs(total)
    return round(error, 6)