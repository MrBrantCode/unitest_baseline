"""
QUESTION:
Implement a function update_adjacency_matrix(dp, N) to update the adjacency matrix dp of a directed weighted graph with N nodes. The function should update dp[i][j] to the minimum of dp[i][j] and dp[i][k] + dp[k][j] for all pairs of nodes (i, j, k). The input dp is a 2D list where dp[i][j] represents the weight of the edge from node i to node j, and N is an integer representing the number of nodes.
"""

from typing import List

def update_adjacency_matrix(dp: List[List[int]], N: int) -> List[List[int]]:
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp[i][k] != float('inf') and dp[k][j] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp