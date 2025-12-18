"""
QUESTION:
Given a 2D-array `edges` representing a graph with an extra edge, find the edge that can be removed to transform the graph back into a tree of N nodes. The graph contains N nodes with unique values ranging from 1 to N. Each element in `edges` is a pair `[u, v]` where `u < v`, representing an undirected edge between nodes `u` and `v`. If multiple solutions exist, return the one that appears last in the 2D-array. The output edge `[u, v]` must satisfy the condition `u < v`. The input 2D-array's size will range between 3 and 1000, and every integer in the array will be between 1 and N. Implement the function `findRedundantConnection(edges)` to solve this problem.
"""

def findRedundantConnection(edges):
    parent = [0] * len(edges)

    def find(x):
        if parent[x] == 0:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX == rootY:
            return False
        parent[rootX] = rootY
        return True

    for x, y in edges:
        if not union(x - 1, y - 1):   
            return [x, y]