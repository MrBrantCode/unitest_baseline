"""
QUESTION:
Find the function g(S, G, L) that calculates the number of sets of size S with greatest common divisor (GCD) greater than or equal to G and least common multiple (LCM) less than or equal to L. The function should return the result modulo 101^4. Implement this function for S = 10^6, G = 10^12, and L = 10^18.
"""

def entance(S, G, L):
    import math
    mod = 101 ** 4
    def ncr(n, r, p):
        num = den = 1
        for i in range(r):
            num = (num * (n - i)) % p
            den = (den * (i + 1)) % p
        return (num * pow(den, p - 2, p)) % p

    total = 0
    for gcd in range(G, L + 1, G):
        x = L // gcd
        if x < S:
            continue
        for choose in range(S, x + 1):
            total += ncr(x, choose, mod)
        total %= mod
    return total