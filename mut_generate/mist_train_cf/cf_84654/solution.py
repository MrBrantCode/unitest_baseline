"""
QUESTION:
Given a square matrix `isConnected` of size `n x n` where `isConnected[i][j]` represents the weight of the direct connection between the `ith` city and the `jth` city, and `isConnected[i][j] = 0` if they are not directly connected, implement a function `findCircleNum(isConnected)` that returns the total number of provinces, where a province is considered a separate province if the total weight of its connections is unique. Note that `1 <= n <= 200`, `isConnected[i][i] == 1`, and `isConnected[i][j] == isConnected[j][i]`.
"""

def findCircleNum(isConnected):
    visited = set()
    n = len(isConnected)

    def dfs(node):
        for nei, val in enumerate(isConnected[node]):
            if val and nei not in visited:
                visited.add(nei)
                dfs(nei)

    provinces = 0
    for i in range(n):
        if i not in visited:
            visited.add(i)
            dfs(i)
            provinces += 1

    return provinces