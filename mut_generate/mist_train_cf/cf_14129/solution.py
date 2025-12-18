"""
QUESTION:
Given two strings, write a function `longest_common_subsequence` that returns the length of the longest common subsequence between the two strings. A subsequence is defined as a sequence that is obtained by deleting some elements from the original sequence, but maintaining the order of the remaining elements.
"""

def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Returns the length of the longest common subsequence between two strings.

    Args:
        text1 (str): The first string.
        text2 (str): The second string.

    Returns:
        int: The length of the longest common subsequence.
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]