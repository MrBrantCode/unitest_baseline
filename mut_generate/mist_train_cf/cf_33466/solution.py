"""
QUESTION:
Write a function `findStronglyConnectedComponents(g)` that takes a directed graph `g` as input, represented as an adjacency list, and returns a list of lists, where each inner list represents a strongly connected component in the graph. The input graph `g` is guaranteed to be represented as a dictionary where `g[i]` is a list containing the indices of the nodes that are adjacent to node `i`, and each node is represented by its index in the adjacency list.
"""

def findStronglyConnectedComponents(graph):
    def dfs1(node, visited, stack):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs1(neighbor, visited, stack)
        stack.append(node)

    def dfs2(node, visited, component):
        visited[node] = True
        component.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs2(neighbor, visited, component)

    n = len(graph)
    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs1(i, visited, stack)

    gr = {i: [] for i in range(n)}
    for i in range(n):
        for j in graph[i]:
            gr[j].append(i)

    visited = [False] * n
    components = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs2(node, visited, component)
            components.append(component)

    return components