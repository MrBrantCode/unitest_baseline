"""
QUESTION:
Implement a function `shortest_distance` that uses Dijkstra's algorithm to find the shortest distance from a starting node `(h, w)` to a destination node `(a, b)` in a weighted directed graph. The graph is represented as a dictionary `alst` where the keys are node coordinates and the values are dictionaries of neighboring nodes with their corresponding edge weights. If there is no edge between two nodes, the weight is infinity. Return the shortest distance to the destination node, or -1 if there is no path.
"""

import heapq

def dijkstra(alst, h, w, a, b):
    dist = {node: float('inf') for node in alst}
    dist[(h, w)] = 0
    toVisit = list(alst.keys())

    while toVisit:
        key = min(toVisit, key=lambda x: dist[x])
        if dist[key] == float('inf'):
            break
        for t in alst[key]:
            val = dist[key]
            dist[t] = min(dist[t], val + alst[key][t])
        toVisit.remove(key)

    return dist[(a, b)] if dist[(a, b)] != float('inf') else -1