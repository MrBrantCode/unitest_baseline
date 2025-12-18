"""
QUESTION:
Write a function named `lcs3(s1, s2, s3)` that finds the length of the longest shared subsequence of characters among three distinct textual strings `s1`, `s2`, and `s3`. Each string can have a length up to 5000 characters and can contain any ASCII characters. The function should optimize for memory consumption and speed, handle edge cases (e.g., multiple longest shared subsequences or no shared subsequences), and be able to identify shared subsequences even if characters appear non-contiguously.
"""

def lcs3(s1, s2, s3):
    m, n, o = len(s1), len(s2), len(s3)
    dp = [[[0 for _ in range(o+1)] for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 0
                elif s1[i-1] == s2[j-1] == s3[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
                    
    return dp[m][n][o]