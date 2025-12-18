"""
QUESTION:
Given a list of edges representing a graph, where each edge is a tuple of two vertices (origin and destination), implement a function `find_cycle_edge` that returns the edge that causes a cycle when added to the graph. The function should utilize the `find(y)` function to get the parent of vertex `y` and the `union(x, y)` function to merge sets containing vertices `x` and `y`, which returns `True` if the merge is successful and `False` if it causes a cycle. The function should return the edge that causes a cycle as a tuple of two vertices, and return an empty tuple if no cycle is found.

Function signature: `def find_cycle_edge(edges: List[Tuple[int, int]]) -> Tuple[int, int]`
"""

from typing import List, Tuple

def find_cycle_edge(edges: List[Tuple[int, int]]) -> Tuple[int, int]:
    parents = {}

    def find(y):
        if y not in parents:
            parents[y] = y
        if parents[y] != y:
            parents[y] = find(parents[y])
        return parents[y]

    def union(x, y):
        parent_x = find(x)
        parent_y = find(y)
        if parent_x == parent_y:
            return False
        parents[parent_x] = parent_y
        return True

    for origin, destination in edges:
        if not union(origin, destination):
            return (origin, destination)
    return ()