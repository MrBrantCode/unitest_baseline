"""
QUESTION:
Given a sequence $a_n$ as the supreme real root of a cubic polynomial $g(x) = x^3 - 2^n \cdot x^2 + n$, find the last eight digits of $\sum \limits_{i = 1}^{30} \lfloor a_i^{987654321} \rfloor$. Note that $\lfloor a \rfloor$ represents the floor function and $a_i > 2^i$ for all $i$.
"""

def entrance(n):
    a = round((2**n+math.sqrt(4**n-4*n))/2)
    result = (30 * (pow(a, 987654321, 10**8))) % (10**8)
    return result