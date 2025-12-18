"""
QUESTION:
Write a function named min_cost that calculates the minimum cost to transform one string into another. The function should take two strings str1 and str2 as input and return the minimum cost. The cost of each operation (insertion, deletion, or replacement) is equal to the absolute difference between the ASCII values of the characters involved.
"""

def min_cost(str1, str2):
    m = len(str1)
    n = len(str2)

    # Initialize the dp matrix
    dp = [[0] * (n+1) for _ in range(m+1)]

    # Fill the first row and column
    for i in range(1, m+1):
        dp[i][0] = i * ord(str1[i-1])  # cost of insertion

    for j in range(1, n+1):
        dp[0][j] = j * ord(str2[j-1])  # cost of deletion

    # Fill the dp matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                replace_cost = abs(ord(str1[i-1]) - ord(str2[j-1]))
                dp[i][j] = min(dp[i-1][j-1] + replace_cost,  # replace
                               dp[i-1][j] + replace_cost,    # delete
                               dp[i][j-1] + replace_cost)    # insert

    return dp[m][n]