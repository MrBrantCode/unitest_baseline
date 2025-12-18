"""
QUESTION:
Implement a function `all_pairs_shortest_paths(vertices, distances)` that computes the shortest paths between all pairs of vertices in a directed graph using the Floyd-Warshall algorithm. The function takes two parameters: a list of vertices in the graph and a dictionary mapping pairs of vertices to their respective distances. The function should return a dictionary representing the shortest distances between all pairs of vertices in the graph.
"""

from typing import List, Dict, Tuple
from math import inf

def all_pairs_shortest_paths(vertices: List[int], distances: Dict[Tuple[int, int], float]) -> Dict[Tuple[int, int], float]:
    dist = { (u, v): inf for u in vertices for v in vertices }
    
    for u, v in distances:
        dist[(u, v)] = distances[(u, v)]
    
    for v in vertices:
        dist[(v, v)] = 0
    
    for interm in vertices:
        for source in vertices:
            for destination in vertices:
                shc = dist[(source, interm)] + dist[(interm, destination)]
                dist[(source, destination)] = min(dist[(source, destination)], shc)

    return dist