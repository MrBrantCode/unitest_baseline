"""
QUESTION:
Compute the value of the function S(N) defined as the sum of G(n) for all positive integers n from 1 to N, where G(n) is the sum of the products of the divisors of all possible partitions of n. The product of divisors of a number n is given by the function D(n), which can be calculated using the formula: D(pq) = D(p)q + pD(q) for any positive integers p, q > 1, and D(p) = 1 for any prime p. Implement the function S(N) with the constraint that the result should be computed modulo 999676999.
"""

def entrance(N):
    G = [0] * (N + 1)
    G[1] = 1
    for n in range(2, N + 1):
        for i in range(1, n):
            G[n] += i * G[n - i] % 999676999
    return sum(G[i] for i in range(1, N + 1)) % 999676999