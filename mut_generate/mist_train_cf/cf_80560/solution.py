"""
QUESTION:
Given an integer `n`, return the number of distinct phone numbers of length `n` that can be dialed using a chess knight on a standard phone keypad, without any repeated consecutive digits. The knight's movements are restricted to two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The answer should be returned modulo `10^9 + 7`. The function name should be `knightDialer`. The constraint is `1 <= n <= 5000`.
"""

def knightDialer(n: int) -> int:
    modulo = 10**9 + 7
    graph = [
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],

        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
    ]  
              
    dp = [[0] * 10 for _ in range(n)]
    dp[0] = [1] * 10

    for i in range(1, n):
        for j in range (10):
            for k, canMove in enumerate(graph[j]):
                if canMove:
                    dp[i][k] = (dp[i][k] + dp[i - 1][j]) % modulo            

    return sum(dp[-1]) % modulo