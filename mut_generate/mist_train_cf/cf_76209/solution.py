"""
QUESTION:
Implement a method named `knightDialer` that takes an integer `n` as input and returns the total number of unique numbers that can be dialed by a knight on a standard phone dial pad in `n` moves. The knight can move from a digit to another if the corresponding keys are adjacent to each other. The result should be returned modulo `10^9 + 7`.
"""

def knightDialer(n: int) -> int:
    modulo = 10 ** 9 + 7

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
        for j in range(10):
            for k, canMove in enumerate(graph[j]):
                if canMove:
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % modulo
        
    return sum(dp[-1]) % modulo