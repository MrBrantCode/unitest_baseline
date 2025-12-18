"""
QUESTION:
Write a function `count_palindromic_substrings(s: str) -> int` that takes in a string `s` of lowercase English letters and returns the count of non-empty palindromic substrings. The input string length is between 1 and 10^5.
"""

def count_palindromic_substrings(s: str) -> int:
    n = len(s)
    MOD = int(1e9 + 7)
    dp = [1] * n
    count = n  # Count of single character palindromes

    for i in range(1, n):
        # Count odd length palindromes with center at i
        l, r = i - 1, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            dp[r] = (dp[r] + dp[l]) % MOD
            l -= 1
            r += 1

        # Count even length palindromes with center between i and i-1
        l, r = i - 1, i
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            dp[r] = (dp[r] + dp[l]) % MOD
            l -= 1
            r += 1

    return count