"""
QUESTION:
Compute the minimum string edit distance between two strings using the Levenshtein distance algorithm. Implement a function `levenshtein_distance(str1, str2)` that calculates the minimum number of operations (insertions, deletions, and substitutions) required to transform `str1` into `str2`. The function should take two strings `str1` and `str2` as input and return the minimum string edit distance. The function should not have any restrictions on the lengths of the input strings.
"""

def levenshtein_distance(str1, str2):
    """
    Compute the minimum string edit distance between two strings using the Levenshtein distance algorithm.

    Args:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    int: The minimum string edit distance between str1 and str2.
    """

    # Create a matrix with dimensions (m+1) x (n+1)
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and first column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    # The minimum string edit distance is stored in the bottom-right cell
    return dp[m][n]