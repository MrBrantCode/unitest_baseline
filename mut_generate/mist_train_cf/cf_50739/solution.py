"""
QUESTION:
Given an undirected, connected graph of N nodes (labelled 0, 1, 2, ..., N-1) represented as a list of adjacency lists `graph`, write a function `shortestPathLength` that determines the length of the shortest path that traverses every node. The function should take `graph` as input and return the minimum length of the path. The constraints are 1 <= graph.length <= 12 and 0 <= graph[i].length < graph.length.
"""

from collections import deque

def shortestPathLength(graph):
    N = len(graph)
    dist = [[float('inf')] * (2**N) for _ in range(N)]
    dq = deque()
    
    # Start from each node
    for node in range(N):
        dq.append((node, 1 << node))  # Using a bitmask to denote nodes visited
        dist[node][1 << node] = 0  # Distance from node to itself is 0
        
    while dq:
        node,mask = dq.popleft()
        for nei in graph[node]:  # Visit all neighbours
            new_mask = mask | (1 << nei)  # Update the mask 
            if dist[nei][new_mask] == float('inf'):  # If this is the first visit
                dq.append((nei,new_mask))
                dist[nei][new_mask] = dist[node][mask] + 1  # We have moved one step
    # Return the min path length when all nodes are visited
    return min(dist[node][(1<<N)-1] for node in range(N))