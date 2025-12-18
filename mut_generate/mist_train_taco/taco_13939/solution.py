"""
QUESTION:
You are given a binary string $s$.

Find the number of distinct cyclical binary strings of length $n$ which contain $s$ as a substring.

The cyclical string $t$ contains $s$ as a substring if there is some cyclical shift of string $t$, such that $s$ is a substring of this cyclical shift of $t$.

For example, the cyclical string "000111" contains substrings "001", "01110" and "10", but doesn't contain "0110" and "10110".

Two cyclical strings are called different if they differ from each other as strings. For example, two different strings, which differ from each other by a cyclical shift, are still considered different cyclical strings.


-----Input-----

The first line contains a single integer $n$ ($1 \le n \le 40$) — the length of the target string $t$.

The next line contains the string $s$ ($1 \le |s| \le n$) — the string which must be a substring of cyclical string $t$. String $s$ contains only characters '0' and '1'.


-----Output-----

Print the only integer — the number of distinct cyclical binary strings $t$, which contain $s$ as a substring.


-----Examples-----
Input
2
0

Output
3
Input
4
1010

Output
2
Input
20
10101010101010

Output
962


-----Note-----

In the first example, there are three cyclical strings, which contain "0" — "00", "01" and "10".

In the second example, there are only two such strings — "1010", "0101".
"""

def count_distinct_cyclical_strings(n: int, s: str) -> int:
    m = len(s)
    z = [[0, 0]]
    for c in s:
        ind = z[-1][c == '1']
        z[-1][c == '1'] = len(z)
        z.append(z[ind][:])
    assert len(z) == m + 1
    z[m][0] = z[m][1] = m
    dp = [0 for _ in range(m + 1)]
    dp[0] = 1
    for i in range(n):
        ndp = [0 for _ in range(m + 1)]
        for i in range(m + 1):
            ndp[z[i][0]] += dp[i]
            ndp[z[i][1]] += dp[i]
        dp = ndp
    res = dp[m]
    for k in range(1, m):
        s0 = 0
        for c in s[-k:]:
            s0 = z[s0][c == '1']
        dp = [0 for _ in range(m + 1)]
        dp[s0] = 1
        for i in range(n - k):
            ndp = [0 for _ in range(m + 1)]
            for i in range(m + 1):
                ndp[z[i][0]] += dp[i]
                ndp[z[i][1]] += dp[i]
            dp = ndp
        for s1 in range(m):
            v = dp[s1]
            for c in s[-k:]:
                if s1 == m:
                    v = 0
                s1 = z[s1][c == '1']
            if s1 == m:
                res += v
    return res