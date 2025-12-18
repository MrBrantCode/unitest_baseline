"""
QUESTION:
Given a 2D array `graph` representing an undirected graph with `n` nodes, where each node is numbered between `0` and `n - 1`, write a function `validTree(n, graph)` that returns `true` if the graph is a tree (i.e., connected and there is exactly one path between any two nodes) and `false` otherwise. 

The input graph is represented as an adjacency list where `graph[u]` is an array of nodes that node `u` is adjacent to. The graph has no self-edges, no parallel edges, and if `v` is in `graph[u]`, then `u` is in `graph[v]`. The number of nodes `n` is between `1` and `100`.
"""

def validTree(n, edges):
    graph = {i:set() for i in range(n)}
    for u, v in edges: # Create adjacency list
        graph[u].add(v)
        graph[v].add(u)
    
    parent = {0:-1}
    stack = [0]
    while stack: # DFS traversal to check cycle
        node = stack[-1]
        if graph[node]:
            nei = graph[node].pop()
            if nei != parent[node]: 
                if nei in parent: # Cycle detected
                    return False
                stack.append(nei)
                parent[nei] = node
        else:
            stack.pop()
    
    return len(parent) == n # Check if graph is connected