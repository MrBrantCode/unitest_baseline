"""
QUESTION:
Write a function `crypticCiphers(n, minValue, group, value)` that takes in the number of members `n`, the minimum required value `minValue`, and two lists `group` and `value` of the same length representing the number of members and the value required for each cipher respectively. 

The function should return the number of ciphers that can be decoded by the group of `n` members, such that the total value is at least `minValue` and the total number of members decoding the ciphers is at most `n`. The return value should be the total count modulo `10^9 + 7`.

Constraints: `1 <= n <= 100`, `0 <= minValue <= 100`, `1 <= len(group) <= 100`, `1 <= group[i] <= 100`, `0 <= value[i] <= 100`, and `len(group) == len(value)`.
"""

MOD = 10**9+7

def crypticCiphers(n, minValue, group, value):
    dp = [[0 for _ in range(101)] for _ in range(101)]
    dp[0][0] = 1
    ciphers = sorted(zip(group, value))

    for g, v in ciphers:
        for i in range(n, g-1, -1):
            for j in range(minValue, -1, -1):
                nextValue = min(100, j + v)
                dp[i][nextValue] = (dp[i][nextValue] + dp[i - g][j]) % MOD

    return sum(dp[n]) % MOD