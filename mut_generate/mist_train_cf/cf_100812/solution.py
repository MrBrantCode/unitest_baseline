"""
QUESTION:
Given a directed graph with N nodes and a list of edges, write a function `max_product_subgraphs(N, edges)` that returns the maximum product of the sizes of two disjoint subgraphs that can be formed by removing one edge. The function should return the result modulo 10^9 + 7.
"""

def max_product_subgraphs(N, edges):
    mod = 10**9 + 7
    
    # initialize dp table
    dp = [[[0 for k in range(N+1)] for j in range(N+1)] for i in range(N+1)]
    
    # fill dp table
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
    
    # find maximum product
    ans = 0
    for j in range(1, N//2+1):
        k = N-j
        ans = max(ans, dp[N-1][j][k])
    
    return ans % mod