"""
QUESTION:
Determine the winner of a two-player game where players take turns removing elements from a list of integers, with the goal of achieving a higher score than the opponent. Write a function `game_winner` that takes a list of integers as input and returns the winner's name ("Alice" or "Bob"). The game starts with Alice if the list has an odd number of elements, and with Bob if the list has an even number of elements. On each turn, the current player removes either the first or last element from the list, increasing their score by the removed element's value. The game ends when the list is empty.
"""

def game_winner(scores):
    n = len(scores)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = scores[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(scores[i] - dp[i + 1][j], scores[j] - dp[i][j - 1])

    return "Alice" if dp[0][n - 1] > 0 else "Bob"