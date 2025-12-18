"""
QUESTION:
Write a function `S(n)` to calculate the total number of lattice points contained within all distinct lattice cubes where the coordinates of all vertices are confined within the range of 0 to `n`, inclusive. The function should return the result modulo 10^9.

Restrictions: 
- The function `S(n)` should take an integer `n` as input.
- The result should be returned modulo 10^9.
"""

modulus = 10**9

def S(n):
    result = 0
    for i in range(n+1):
        Ni = (i + 1) ** 3
        Ci = (n - i + 1) ** 3
        result += Ni * Ci
        result %= modulus
    return result