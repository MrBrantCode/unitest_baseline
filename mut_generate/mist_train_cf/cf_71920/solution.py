"""
QUESTION:
Compute the value of F(N) modulo 1,000,000,007, where F(N) is defined as the sum of R(n^4 + 4) for all n from 1 to N, and R(n) is the count of retractions for a given n. A retraction is a function f_{n,a,b}(x) ≡ a*x + b mod n, where 0 < a < n, 0 ≤ b < n, and 0 ≤ x < n, such that f_{n,a,b}(f_{n,a,b}(x)) ≡ f_{n,a,b}(x) mod n for every integer 0 ≤ x < n.
"""

MOD = 10**9 + 7

def entrance(N):
    def R(n):
        if n == 2:
            return 1
        else:
            return n - 1

    result = 0
    for n in range(1, N+1):
        result = (result + R((n**4 + 4) % MOD)) % MOD
    return result