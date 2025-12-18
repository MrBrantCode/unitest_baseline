"""
QUESTION:
Implement a function `countClusters(graph)` that takes an undirected graph represented as an adjacency list as input and returns the total number of clusters present in the graph. The function should work with any given adjacency list, where each key represents a vertex and its corresponding value is a list of neighboring vertices. The function should not take any additional parameters other than the adjacency list. The graph may contain any number of vertices and edges, and the function should handle these variations correctly.
"""

def countClusters(graph):
    def dfs(vertex, visited, cluster):
        visited.add(vertex)
        cluster.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor, visited, cluster)

    num_clusters = 0
    visited_vertices = set()
    for vertex in graph:
        if vertex not in visited_vertices:
            cluster = []
            dfs(vertex, visited_vertices, cluster)
            num_clusters += 1
    return num_clusters