"""
QUESTION:
Write a function `max_product_subgraphs(N, edges)` that takes as input the number of nodes `N` in a directed graph and a list of edges `edges`, where each edge is represented as a pair of node indices. The function should return the maximum product of the sizes of two disjoint subgraphs that can be obtained by removing one edge from the graph, modulo 10^9 + 7.
"""

def max_product_subgraphs(N, edges):
    mod = 10**9 + 7

    dp = [[[0 for k in range(N+1)] for j in range(N+1)] for i in range(N+1)]

    for i in range(1, N):
        for j in range(1, N-i+1):
            k = i+j
            for edge in edges:
                if j <= edge[0] < k and j <= edge[1] < k:
                    dp[i][edge[0]][edge[1]] = max(dp[i][edge[0]][edge[1]], dp[i-1][edge[0]-1][edge[1]])
                    dp[i][edge[0]][edge[1]] = max(dp[i][edge[0]][edge[1]], dp[i-1][edge[0]][edge[1]-1])
                    dp[i][edge[0]][edge[1]] %= mod
                else:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k])
                    dp[i][j][k] = max(dp[i][j][k], j*(N-k))
                    dp[i][j][k] %= mod

    ans = 0
    for j in range(1, N//2+1):
        k = N-j
        ans = max(ans, dp[N-1][j][k])

    return ans % mod