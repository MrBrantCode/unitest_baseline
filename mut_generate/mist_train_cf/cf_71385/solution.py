"""
QUESTION:
Write a function `shortestPathLength(graph)` that takes a connected, undirected graph `graph` of `N` nodes as input, represented as an adjacency list, and returns the length of the shortest path that traverses every node. The graph is represented as a list of lists, where `graph[i]` is a list of nodes connected to node `i`. The function should assume that the graph length does not exceed 12 and that the start and end nodes can be any node, with the possibility of revisiting nodes and reusing edges.
"""

def shortestPathLength(graph):
    N = len(graph)
    final = (1 << N) - 1
    dist = [[float('inf')] * (1 << N) for _ in range(N)]
    q = [x for y in [[(i, 1 << i, 0)] for i in range(N)] for x in y]

    for node, visited, path in q:
        if visited == final: return path
        for nei in graph[node]:
            v = visited | (1 << nei)
            if path + 1 < dist[nei][v]:
                dist[nei][v] = path + 1
                q.append((nei, v, path + 1))
    return -1