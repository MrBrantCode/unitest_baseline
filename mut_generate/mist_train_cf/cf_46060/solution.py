"""
QUESTION:
Write a function `derangement(n)` that calculates the number of derangements for a set of size `n`, where `n` is an integer ranging from 1 to 10^6. The function should return the result modulo 10^9 + 7.
"""

def derangement(n):
    mod = 10**9 + 7
    der = [0, 0] + [0]*n
    der[0] = 1
    der[1] = 0
    der[2] = 1
    for i in range(3, n+1):
        der[i] = ((i-1) * (der[i-1] + der[i-2])) % mod
    return der[n]