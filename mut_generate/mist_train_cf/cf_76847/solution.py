"""
QUESTION:
Define the function M(x) that represents the number of cycles needed to restore the original configuration given x bowls. Given that for any non-negative integer k, M(2^k + 1) = (2^k + 1) * 2 * M(2^(k-1) + 1) and M(1) = 1, compute the sum of M(2^k + 1) for k ranging from 0 to 10^18 modulo 7^9.
"""

def entrance(x):
    MOD = 7**9
    res = 1
    for k in range(x):
        res = res * ((2**k + 1) % MOD) * 2 % MOD
    return res