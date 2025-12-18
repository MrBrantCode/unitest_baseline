"""
QUESTION:
Given a string `s` consisting of '1' and '0', find the number of ways to partition `s` into three parts such that each part contains an equal number of '1's and the number of '0's in each part is a multiple of 2. The function name is `numWays` and it should return the result modulo `10**9 + 7`.
"""

def numWays(s: str) -> int:
    one_sum, zero_sum = [], []
    one_count, zero_count = 0, 0
    for c in s:
        if c == '1':
            one_count += 1
        else:
            zero_count += 1
        one_sum.append(one_count)
        zero_sum.append(zero_count)

    if one_count % 3 != 0:
        return 0

    if one_count == 0:
        return ((zero_count - 1) * (zero_count - 2) // 2) % (10**9 + 7)

    one_count //= 3
    one_indices = [i for i, v in enumerate(one_sum) if v == one_count]

    dp = [[[0]*3 for _ in range(4)] for _ in range(len(s) + 1)]
    dp[0][0][0] = 1

    for i in range(len(s)):
        for j in range(4):
            for x in range(3):
                if one_sum[i] == j * one_count and zero_sum[i] - j * 2 == x:
                    dp[i+1][j][x] = (dp[i+1][j][x] + dp[i][j-1][2]) % (10**9 + 7)
                dp[i+1][j][x] = (dp[i+1][j][x] + dp[i][j][(zero_sum[i] - j * 2)%3]) % (10**9 + 7)

    return dp[-1][3][0]