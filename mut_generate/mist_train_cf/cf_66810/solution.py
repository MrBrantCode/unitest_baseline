"""
QUESTION:
Given a positive integer n, define f(n) as the count of pairs (p,q) of positive integers satisfying 1 ≤ p < q ≤ n and p and q are 2-friendly, i.e., gcd(p,q) = 2^t, t > 0. Implement a function f(n) that calculates f(n) modulo 1,000,000,007.
"""

MOD = int(1e9 + 7)

def f(n):
    f_values = [0] * ((n // 2) + 1)
    h_values = [0] * ((n // 2) + 1)

    ans = 0
    n //= 2
    for i in range(1, n+1):
        h_values[i] = n // i - 1
    for i in range(1, n+1):
        f_values[i] = (i * (i-1)) // 2
        j = 2
        while i * j <= n:
            f_values[i] -= f_values[i * j]
            j += 1
        ans = (ans + i * f_values[i]) % MOD
    return ans * 2 % MOD