"""
QUESTION:
Little Petya loves counting. He wants to count the number of ways to paint a rectangular checkered board of size n × m (n rows, m columns) in k colors. Besides, the coloring should have the following property: for any vertical line that passes along the grid lines and divides the board in two non-empty parts the number of distinct colors in both these parts should be the same. Help Petya to count these colorings.

Input

The first line contains space-separated integers n, m and k (1 ≤ n, m ≤ 1000, 1 ≤ k ≤ 106) — the board's vertical and horizontal sizes and the number of colors respectively.

Output

Print the answer to the problem. As the answer can be quite a large number, you should print it modulo 109 + 7 (1000000007).

Examples

Input

2 2 1


Output

1


Input

2 2 2


Output

8


Input

3 2 2


Output

40
"""

def count_colorings(n: int, m: int, k: int) -> int:
    mod = 10**9 + 7
    
    if m == 1:
        return pow(k, n, mod)
    
    fac = [1]
    ifac = [1]
    tav = [0]
    
    for i in range(1, max(k + 1, n + 1)):
        fac.append(fac[i - 1] * i % mod)
    
    for i in range(1, min(k + 1, n + 1)):
        ifac.append(ifac[i - 1] * pow(i, mod - 2, mod) % mod)
        tav.append(pow(i, n * (m - 2), mod))
    
    if m == 2:
        tav[0] = 1
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(i, 1, -1):
            dp[j] = (j * dp[j] + dp[j - 1]) % mod
    
    ans = 0
    for i in range(1, min(k + 1, n + 1)):
        for j in range(0, i + 1):
            if 2 * i - j > k:
                continue
            ans = (ans + dp[i] * dp[i] * fac[i] * fac[i] % mod * tav[j] * ifac[i - j] * fac[k] % mod * pow(fac[k - 2 * i + j], mod - 2, mod) * ifac[i - j] * ifac[j]) % mod
    
    return ans