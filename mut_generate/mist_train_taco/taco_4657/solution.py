"""
QUESTION:
You are given a positive integer $n$. Since $n$ may be very large, you are given its binary representation.

You should compute the number of triples $(a,b,c)$ with $0 \leq a,b,c \leq n$ such that $a \oplus b$, $b \oplus c$, and $a \oplus c$ are the sides of a non-degenerate triangle.

Here, $\oplus$ denotes the bitwise XOR operation .

You should output the answer modulo $998\,244\,353$.

Three positive values $x$, $y$, and $z$ are the sides of a non-degenerate triangle if and only if $x+y>z$, $x+z>y$, and $y+z>x$.


-----Input-----

The first and only line contains the binary representation of an integer $n$ ($0 < n < 2^{200000}$) without leading zeros.

For example, the string 10 is the binary representation of the number $2$, while the string 1010 represents the number $10$.


-----Output-----

Print one integer — the number of triples $(a,b,c)$ satisfying the conditions described in the statement modulo $998\,244\,353$.


-----Examples-----

Input
101
Output
12
Input
1110
Output
780
Input
11011111101010010
Output
141427753


-----Note-----

In the first test case, $101_2=5$.

The triple $(a, b, c) = (0, 3, 5)$ is valid because $(a\oplus b, b\oplus c, c\oplus a) = (3, 6, 5)$ are the sides of a non-degenerate triangle.

The triple $(a, b, c) = (1, 2, 4)$ is valid because $(a\oplus b, b\oplus c, c\oplus a) = (3, 6, 5)$ are the sides of a non-degenerate triangle.

The $6$ permutations of each of these two triples are all the valid triples, thus the answer is $12$.

In the third test case, $11\,011\,111\,101\,010\,010_2=114\,514$. The full answer (before taking the modulo) is $1\,466\,408\,118\,808\,164$.
"""

def count_valid_triples(binary_n: str) -> int:
    MOD = 998244353
    TRANS = [6, 3, 7, 4, 1, 0]
    
    dp = [0] * 7 + [1]
    for c in map(int, binary_n):
        dp1 = [0] * 8
        for i in range(8):
            for k in TRANS:
                if c:
                    dp1[k & i] += dp[i]
                elif k & i == 0:
                    dp1[i] += dp[i]
        dp = [x % MOD for x in dp1]
    
    n = int(binary_n, base=2) + 1
    result = (n ** 3 + 3 * n ** 2 - n - 3 * sum(dp)) % MOD
    return result