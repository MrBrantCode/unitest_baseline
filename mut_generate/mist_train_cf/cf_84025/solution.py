"""
QUESTION:
Compute `S(n)` for `n = 10000`, where `S(n)` denotes the quantity of dynamical polynomials of degree `n`. A dynamical polynomial is a monic polynomial `f(x)` with integer coefficients that divides `f(x^2-2)`. The answer should be presented modulo `998244353`.
"""

MOD = 998244353

def entrance(n):
    MAX_N = 2*n + 1
    fac = [1]*(MAX_N+1)
    inv = [1]*(MAX_N+1)

    for i in range(1, MAX_N+1):
        fac[i] = (fac[i-1]*i)%MOD
        inv[i] = pow(fac[i], MOD-2, MOD)

    def C(a, b):
        return fac[a]*inv[b]*inv[a-b]%MOD

    S = C(2*n, n)
    S = (S - C(2*n, n-1))*pow(2,MOD-2,MOD)%MOD
    return S