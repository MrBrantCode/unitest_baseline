"""
QUESTION:
Define the AND-product of x and y, denoted by x ⊗ y, similar to a long multiplication in base 2, except that the intermediate results are ANDed instead of the usual integer addition. Define Q(n) = 13^(⊗n). Given that Q(n) has a periodic nature with a period T = 1147036, write a function Q(n) that calculates Q(n % T) and returns the result modulo 10^9 + 7.
"""

mod = 10**9+7
T = 1147036 

def power(a, b, m):
    a = a % m
    result = 1
    while b > 0:
        if b % 2:
            result = (result * a) % m
        a = (a*a) % m
        b //= 2
    return result

def Q(n):
    n = n % T
    if n == 0: return 13 % mod
    if n == 1: return 169 % mod 
    x = Q(n//2)
    if n % 2:
        return (power(x, 2, mod) * 13) % mod
    else:
        return power(x, 2, mod)