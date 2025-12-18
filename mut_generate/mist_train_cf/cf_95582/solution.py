"""
QUESTION:
Create a function `LCSAlternate(string1, string2)` that takes two strings as input and returns the longest common subsequence that consists of alternating characters from the two strings. If there are multiple valid subsequences of the same length, return the one with the smallest lexicographical order. The strings may contain duplicate characters and the subsequence must be in alternating order, i.e., it cannot have two consecutive characters from the same string.
"""

def LCSAlternate(string1, string2):
    n = len(string1)
    m = len(string2)

    # Initialize dp array
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize first row and column
    for i in range(n + 1):
        dp[i][0] = 0
    for j in range(m + 1):
        dp[0][j] = 0

    # Calculate longest common subsequence length
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-2][j-2] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Retrieve longest common subsequence
    result = ""
    i = n
    j = m

    while i > 0 and j > 0:
        if string1[i-1] == string2[j-1]:
            result += string1[i-1]
            i -= 2
            j -= 2
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return result[::-1]