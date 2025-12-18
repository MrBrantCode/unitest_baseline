"""
QUESTION:
Write a function `lcs(X, Y)` that takes two distinct textual strings `X` and `Y` as input and returns the lengthiest shared subsequence of characters within them. The output should be in the format: "The longest common subsequence is 'XXXXX' and its length is YY". The function should use dynamic programming to build a 2D table where each cell contains the length of the longest common subsequence of the substrings of `X` and `Y`. The function should then use this table to construct the longest common subsequence.
"""

def lcs(X, Y):
    """
    This function takes two distinct textual strings X and Y as input and returns 
    the lengthiest shared subsequence of characters within them.

    Parameters:
    X (str): The first input string.
    Y (str): The second input string.

    Returns:
    str: The longest common subsequence and its length.
    """

    m = len(X)
    n = len(Y)
    dp = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    index = dp[m][n]
    lcs = [""] * (index+1)
    lcs[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)