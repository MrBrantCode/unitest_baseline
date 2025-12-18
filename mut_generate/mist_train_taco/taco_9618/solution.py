"""
QUESTION:
Given is an integer N. Snuke will choose integers s_1, s_2, n_1, n_2, u_1, u_2, k_1, k_2, e_1, and e_2 so that all of the following six conditions will be satisfied:

* 0 \leq s_1 < s_2
* 0 \leq n_1 < n_2
* 0 \leq u_1 < u_2
* 0 \leq k_1 < k_2
* 0 \leq e_1 < e_2
* s_1 + s_2 + n_1 + n_2 + u_1 + u_2 + k_1 + k_2 + e_1 + e_2 \leq N



For every possible choice (s_1,s_2,n_1,n_2,u_1,u_2,k_1,k_2,e_1,e_2), compute (s_2 − s_1)(n_2 − n_1)(u_2 − u_1)(k_2 - k_1)(e_2 - e_1), and find the sum of all computed values, modulo (10^{9} +7).

Solve this problem for each of the T test cases given.

Constraints

* All values in input are integers.
* 1 \leq T \leq 100
* 1 \leq N \leq 10^{9}

Input

Input is given from Standard Input in the following format:


T
\mathrm{case}_1
\vdots
\mathrm{case}_T


Each case is given in the following format:


N


Output

Print T lines. The i-th line should contain the answer to the i-th test case.

Example

Input

4
4
6
10
1000000000


Output

0
11
4598
257255556
"""

def compute_snuke_sum(T: int, cases: list) -> list:
    mod = pow(10, 9) + 7
    inv = [0, 1]
    fact = [1, 1]
    ifact = [1, 1]
    
    # Precompute necessary values for factorials and inverses
    for i in range(2, 16):
        inv.append(inv[mod % i] * (mod - mod // i) % mod)
        fact.append(i * fact[-1] % mod)
        ifact.append(ifact[-1] * inv[i] % mod)
    
    def c(n, r):
        a = 1
        for i in range(r):
            a *= n - i
            a %= mod
        return a * ifact[r] % mod
    
    results = []
    
    for n in cases:
        ans = 0
        n -= 5
        for o in range(12):
            m = n - o
            if m < 0 or m & 1:
                continue
            ans += c(11, o) * c(m // 2 + 15, 15)
            ans %= mod
        results.append(ans)
    
    return results