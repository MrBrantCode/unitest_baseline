"""
QUESTION:
You are given a grid, consisting of $2$ rows and $n$ columns. Each cell of this grid should be colored either black or white.

Two cells are considered neighbours if they have a common border and share the same color. Two cells $A$ and $B$ belong to the same component if they are neighbours, or if there is a neighbour of $A$ that belongs to the same component with $B$.

Let's call some bicoloring beautiful if it has exactly $k$ components.

Count the number of beautiful bicolorings. The number can be big enough, so print the answer modulo $998244353$.


-----Input-----

The only line contains two integers $n$ and $k$ ($1 \le n \le 1000$, $1 \le k \le 2n$) — the number of columns in a grid and the number of components required.


-----Output-----

Print a single integer — the number of beautiful bicolorings modulo $998244353$.


-----Examples-----
Input
3 4

Output
12

Input
4 1

Output
2

Input
1 2

Output
2



-----Note-----

One of possible bicolorings in sample $1$: [Image]
"""

def count_beautiful_bicolorings(n, k):
    mod = 998244353
    dp = [[0] * 4 for _ in range(k + 2)]
    dp[1][0] = 1
    dp[1][3] = 1
    dp[2][1] = 1
    dp[2][2] = 1
    
    for i in range(2, n + 1):
        new = [[0] * 4 for _ in range(k + 2)]
        for j in range(1, k + 2):
            for l in range(4):
                new[j][l] = (dp[j][l] % mod + new[j][l] % mod) % mod
                if l == 0 or l == 3:
                    new[j][l] = (dp[j - 1][l ^ 3] % mod + new[j][l] % mod) % mod
                    new[j][l] = (dp[j][1] % mod + dp[j][2] % mod + new[j][l] % mod) % mod
                elif l == 1 or l == 2:
                    new[j][l] = (dp[j - 1][0] % mod + dp[j - 1][3] % mod + new[j][l] % mod) % mod
                    if j - 2 >= 0:
                        new[j][l] = (dp[j - 2][l ^ 3] % mod + new[j][l] % mod) % mod
        dp = new
    
    return sum(dp[k]) % mod