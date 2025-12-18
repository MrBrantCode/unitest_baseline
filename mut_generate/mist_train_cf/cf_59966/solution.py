"""
QUESTION:
Define a function `calculateFourTileIntersect(k, MOD)` that calculates `f(10^k)`, the number of points where four tiles intersect in the tiling configuration `T(n)`, modulo `17^7`. The input is `k`, a large integer, and `MOD = 17^7`. The function should use modular exponentiation to efficiently compute the result.
"""

def entance(k, MOD):
    period = 16*(17**6)
    def power_mod(n, m, MOD):
        if m==0: return 1
        half = power_mod(n, m//2, MOD)
        if m%2==0:
            return (half**2)%MOD
        else:
            return ((half**2)*n)%MOD

    powMod = power_mod(10, k, period)
    return (power_mod(4, powMod, MOD) - 1) % MOD