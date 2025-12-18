"""
QUESTION:
Write a function `solve(h, w)` that calculates the sum of the number of strongly connected components in all possible directed graphs on an `h x w` lattice grid, modulo `1,000,000,007`.
"""

def solve(h, w):
    MOD = 10**9+7
    INV = []
    FAC = []
    FAC_INV = []

    # Precomputation of factorial, factorial of inverse, and inverse
    FAC.append(1)
    FAC_INV.append(1)
    INV.append(0)
    INV.append(1)
    for i in range(2, h + w + 5):
        FAC.append(FAC[-1] * i % MOD)
        INV.append((MOD - MOD // i) * INV[MOD % i] % MOD)
        FAC_INV.append(FAC_INV[-1] * INV[-1] % MOD)

    def get(n, m):
        # Utilize Combinatorial Number Theorem to compute Binomial Coefficient
        return FAC[n] * FAC_INV[m] % MOD * FAC_INV[n - m] % MOD

    if h == 1:
        return pow(2, w, MOD) 
    if w == 1:
        return pow(2, h, MOD)
    return (solve(h-1, w) + solve(h, w-1) + get(h+w-2, h-1)) % MOD