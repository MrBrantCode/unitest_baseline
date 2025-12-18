"""
QUESTION:
Given an array of integers `coins` representing coin values in a row, write a function `maxScoreDifference` that returns the maximum possible difference in scores between Alice and Bob when they play a game where they alternately remove the leftmost or rightmost coin and receive points equal to the sum of the remaining coins' values. Assume both players play optimally and the game ends when all coins are removed. The length of the input array `coins` is between 2 and 1000, and each coin value is between 1 and 1000.
"""

def maxScoreDifference(coins):
    n = len(coins)
    dp = [[0]*n for _ in range(n)]
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + coins[i]
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j] = max(prefix[j+1]-prefix[i+1]-dp[i+1][j], prefix[j]-prefix[i]-dp[i][j-1])
    return dp[0][n-1]