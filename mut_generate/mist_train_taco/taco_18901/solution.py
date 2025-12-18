"""
QUESTION:
Find the number, modulo 998244353, of sequences of length N consisting of 0, 1 and 2 such that none of their contiguous subsequences totals to X.

Constraints

* 1 \leq N \leq 3000
* 1 \leq X \leq 2N
* N and X are integers.

Input

Input is given from Standard Input in the following format:


N X


Output

Print the number, modulo 998244353, of sequences that satisfy the condition.

Examples

Input

3 3


Output

14


Input

8 6


Output

1179


Input

10 1


Output

1024


Input

9 13


Output

18402


Input

314 159


Output

459765451
"""

def count_valid_sequences(N, X, MOD=998244353):
    def modfac(n, MOD):
        f = 1
        factorials = [1]
        for m in range(1, n + 1):
            f *= m
            f %= MOD
            factorials.append(f)
        inv = pow(f, MOD - 2, MOD)
        invs = [1] * (n + 1)
        invs[n] = inv
        for m in range(n, 1, -1):
            inv *= m
            inv %= MOD
            invs[m - 1] = inv
        return (factorials, invs)

    def modnCr(n, r, mod, fac, inv):
        return fac[n] * inv[n - r] * inv[r] % mod

    (fac, inv) = modfac(N + 10, MOD)
    ans = 0
    for two in range(N + 1):
        for one in range(N + 1):
            if one + two > N:
                break
            dist = one + two * 2
            zero = modnCr(N, one + two, MOD, fac, inv)
            now = 0
            if dist < X:
                now = modnCr(one + two, one, MOD, fac, inv) * zero
            elif dist == X:
                continue
            elif dist < 2 * X:
                if (dist - X) % 2 == 0:
                    continue
                dtwo = two - (dist - X + 1)
                if dtwo >= 0:
                    now = modnCr(one + dtwo, one, MOD, fac, inv) * zero
            elif X % 2 == 1 and one == 0:
                now = zero
            ans += now
            ans %= MOD
    return ans