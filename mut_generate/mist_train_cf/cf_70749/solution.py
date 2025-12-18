"""
QUESTION:
Compute the value of Q(n) where Q(n) is the sum of E(904961, i) for i from 1 to n. The function E(m, n) is the greatest integer k such that 2^k divides S((p_m#)^n) where S(n) represents the quantity of unique pairs (a, b) of distinct divisors of a number n where a is a divisor of b.
"""

def compute_Q(n):
    return 904960 * n * (n+1) // 2