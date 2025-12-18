"""
QUESTION:
Implement the function `connectedComponents` that determines the number of connected components in an undirected graph. The function takes in three parameters: the number of vertices `n`, the number of edges `m`, and the list of edges. The graph is represented using an adjacency list, where each edge is represented as a pair of vertices. The function should return the number of connected components in the graph.
"""

def connectedComponents(n, m, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    visited_nodes = set()
    components = 0
    for node in range(1, n + 1):
        if node not in visited_nodes:
            dfs(node, visited_nodes)
            components += 1

    return components