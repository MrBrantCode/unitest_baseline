"""
QUESTION:
Fox Ciel studies number theory.

She thinks a non-empty set S contains non-negative integers is perfect if and only if for any $a, b \in S$ (a can be equal to b), $(a \text{xor} b) \in S$. Where operation xor means exclusive or operation (http://en.wikipedia.org/wiki/Exclusive_or).

Please calculate the number of perfect sets consisting of integers not greater than k. The answer can be very large, so print it modulo 1000000007 (10^9 + 7).


-----Input-----

The first line contains an integer k (0 ≤ k ≤ 10^9).


-----Output-----

Print a single integer — the number of required sets modulo 1000000007 (10^9 + 7).


-----Examples-----
Input
1

Output
2

Input
2

Output
3

Input
3

Output
5

Input
4

Output
6



-----Note-----

In example 1, there are 2 such sets: {0} and {0, 1}. Note that {1} is not a perfect set since 1 xor 1 = 0 and {1} doesn't contain zero.

In example 4, there are 6 such sets: {0}, {0, 1}, {0, 2}, {0, 3}, {0, 4} and {0, 1, 2, 3}.
"""

def count_perfect_sets(k: int) -> int:
    MOD = 10 ** 9 + 7
    bink = list(map(int, bin(k)[2:]))
    N = len(bink)
    dp = [[[0, 0] for j in range(i + 2)] for i in range(N + 1)]
    dp[0][0][1] = 1
    
    for i in range(1, N + 1):
        for j in range(i + 1):
            dp[i][j][0] += 2 ** j * dp[i - 1][j][0]
            if j:
                dp[i][j][0] += dp[i - 1][j - 1][0]
            odd = 2 ** (j - 1) if j else 0
            even = 2 ** j - odd
            if bink[i - 1] == 1:
                dp[i][j][0] += even * dp[i - 1][j][1]
            if bink[i - 1] == 0:
                dp[i][j][1] += even * dp[i - 1][j][1]
            else:
                dp[i][j][1] += odd * dp[i - 1][j][1]
                if j:
                    dp[i][j][1] += dp[i - 1][j - 1][1]
    
    ans = sum(map(sum, dp[-1]))
    return ans % MOD