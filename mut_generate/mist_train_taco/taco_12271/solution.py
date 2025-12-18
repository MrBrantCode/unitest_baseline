"""
QUESTION:
Consider a regular polygon with N vertices labelled 1..N. In how many ways can you draw K diagonals such that no two diagonals intersect at a point strictly inside the polygon? A diagonal is a line segment joining two non adjacent vertices of the polygon.

Input: 

The first line contains the number of test cases T. Each of the next T lines contain two integers N and K.

Output: 

Output T lines, one corresponding to each test case. Since the answer can be really huge, output it modulo 1000003.

Constraints: 

1 <= T <= 10000 

4 <= N <= 10^9 

1 <= K <= N 

Sample Input: 

3 

4 1 

5 2 

5 3

Sample Output: 

2 

5 

0

Explanation:

For the first case, there are clearly 2 ways to draw 1 diagonal - 1 to 3, or 2 to 4. (Assuming the vertices are labelled 1..N in cyclic order). 

For the third case, at most 2 non-intersecting diagonals can be drawn in a 5-gon, and so the answer is 0.
"""

MOD = 1000003

def inv(x):
    return pow(x, MOD - 2, MOD)

Fact = [1] * MOD
for i in range(2, MOD):
    Fact[i] = i * Fact[i - 1] % MOD

def fact_val(n):
    q = MOD
    v = 0
    while q <= n:
        v += n // q
        q *= MOD
    return v

def fact(n):
    (q, r) = divmod(n, MOD)
    return pow(Fact[MOD - 1], q, MOD) * Fact[q] * Fact[r] % MOD

def binom(n, p):
    assert 0 <= p <= n
    val = fact_val(n) - fact_val(p) - fact_val(n - p)
    f = fact(n) * inv(fact(p)) * inv(fact(n - p)) % MOD
    return (f, val)

def count_non_intersecting_diagonals(N, K, MOD=1000003):
    n = N - 3
    if K > n:
        return 0
    (f1, v1) = binom(n + K + 2, K)
    (f2, v2) = binom(n, K)
    v3 = 0
    K_prime = K + 1
    while K_prime % MOD == 0:
        v3 += 1
        K_prime //= MOD
    if v1 + v2 - v3 > 0:
        return 0
    assert v1 + v2 == v3
    return f1 * f2 * inv(K_prime) % MOD