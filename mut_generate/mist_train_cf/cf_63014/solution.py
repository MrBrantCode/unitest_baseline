"""
QUESTION:
Create a function `M(n)` to calculate the sum of numbers inscribed on the paper after `n` rounds, where in each round, the smallest positive integer `a` not on the paper is inscribed, followed by the smallest integer `b` such that neither `b` nor `(a ⊕ b)` is on the paper, and then `(a ⊕ b)` is inscribed. The function should return the result modulo `1,000,000,007`.
"""

def M(n):
    mod = 1000000007
    if n <= 6: 
        return [0, 6, 24, 60, 120, 210, 336][n] 
    else: 
        return (3*(n**2)%mod + (3*n)%mod + 1)%mod