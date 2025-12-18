"""
QUESTION:
Write a function `numDecodings` that takes a string `s` composed solely of digits as input and returns the number of possible ways to decode it using the standard ordering of letters with `A` mapped to `1`, `B` mapped to `2`, and so on, up to `Z` mapped to `26`. The function should handle strings of length between 1 and 100.
"""

def numDecodings(s: str) -> int:
    if not s:
        return 0

    dp = [0 for _ in range(len(s) + 1)]

    dp[0] = 1 
    dp[1] = 0 if s[0] == "0" else 1

    for i in range(2, len(s) + 1):
        if s[i-1] != "0":
            dp[i] += dp[i - 1]

        if "10" <= s[i-2:i] <= "26":
            dp[i] += dp[i - 2]
    return dp[len(s)]