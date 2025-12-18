"""
QUESTION:
Write a function named `shortest_path` that uses dynamic programming to find the shortest path between two nodes in a weighted graph. The function should take as input a 2D list `graph` representing the weighted graph and two integers `start` and `end` representing the start and end nodes, and return the shortest distance between the start and end nodes. The graph is represented as an adjacency matrix where `graph[i][j]` represents the weight of the edge from node `i` to node `j`, or 0 if there is no edge. The function should return -1 if there is no path between the start and end nodes.
"""

def shortest_path(graph, start, end):
    n = len(graph)
    dp = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] != 0 and graph[k][j] != 0:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    
    return dp[start][end] if dp[start][end] != float('inf') else -1