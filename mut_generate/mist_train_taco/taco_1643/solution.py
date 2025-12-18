"""
QUESTION:
Count the number of prime numbers less than a non-negative number, n.

Example:


Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

def count_primes_less_than(n: int) -> int:
    n = max(0, n - 1)
    if type(n) is not int:
        n = int(n)
    if n < 6:
        return [0, 0, 1, 2, 2, 3][n]

    def Phi(m, b):
        if not b:
            return m
        if not m:
            return 0
        if m >= 800:
            return Phi(m, b - 1) - Phi(m // primes[b - 1], b - 1)
        t = b * 800 + m
        if not Phi_memo[t]:
            Phi_memo[t] = Phi(m, b - 1) - Phi(m // primes[b - 1], b - 1)
        return Phi_memo[t]

    root2 = int(n ** (1.0 / 2))
    root3 = int(n ** (1.0 / 3))
    top = n // root3 + 1
    sieve = [0, 0] + [1] * (top - 2)
    pi = [0, 0]
    primes = []
    t = 0
    for i in range(2, top):
        if sieve[i] == 1:
            t += 1
            primes.append(i)
            sieve[i::i] = [0] * len(sieve[i::i])
        pi.append(t)
    (a, b) = (pi[root3 + 1], pi[root2 + 1])
    Phi_memo = [0] * ((a + 1) * 800)
    return Phi(n, a) + a - 1 - sum((pi[n // p] - pi[p] + 1 for p in primes[a:b]))