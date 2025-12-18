"""
QUESTION:
Write a function `S(N)` that calculates the sum of the steps required to find the highest common factor (HCF) for all pairs of numbers (x, y) where 1 ≤ x, y ≤ N using Euclid's algorithm. The function should take an integer N as input and return the sum of the steps required to find the HCF for all pairs. Note that the naive approach may not be feasible for large inputs due to its time complexity, so an efficient algorithm or mathematical formula is required.
"""

def S(N):
    """
    Calculate the sum of the steps required to find the HCF for all pairs of numbers (x, y) where 1 ≤ x, y ≤ N.

    Args:
    N (int): The input integer.

    Returns:
    int: The sum of the steps required to find the HCF for all pairs.
    """
    def euler_totient(n):
        result = n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n //= p
                result -= result // p
            p += 1
        if n > 1:
            result -= result // n
        return result

    total_steps = 0
    for d in range(1, N + 1):
        total_steps += euler_totient(d) * (N // d) * ((N // d) - 1)
    return total_steps