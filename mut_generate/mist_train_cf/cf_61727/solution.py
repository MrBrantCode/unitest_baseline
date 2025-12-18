"""
QUESTION:
Write a function `countComponents` that takes three parameters: `n` (the number of nodes in a graph), `edges` (an array of weighted edges where each edge is represented as `[ai, bi, wi]`), and `k` (the minimum total weight of edges in a connected component). The function should return the number of connected components in the graph where the total weight of the edges in the component is greater than `k`. The function should work under the constraints: `1 <= n <= 2000`, `1 <= edges.length <= 5000`, and `edges[i].length == 3`.
"""

def countComponents(n, edges, k):
    parent = list(range(n))
    componentWeight, counter = [0] * n, 0
    edges.sort(key=lambda x:-x[2])

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y, w):
        nonlocal counter
        px, py = find(x), find(y)
        if px != py:
            if componentWeight[px] > k:
                counter -= 1
            if componentWeight[py] > k:
                counter -= 1
            parent[px] = py
            componentWeight[py] += (componentWeight[px] + w)
            if componentWeight[py] > k:
                counter += 1

    for x, y, w in edges:
        union(x, y, w)

    return counter