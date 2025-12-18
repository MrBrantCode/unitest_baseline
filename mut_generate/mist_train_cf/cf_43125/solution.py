"""
QUESTION:
Implement a function `has_circular_dependency(dependencies)` that checks for circular dependencies in a given list of dependencies, where each dependency is a tuple of two elements representing the source and target. The function should return True if a circular dependency is found and False otherwise. The function should take a list of tuples as input and return a boolean value.
"""

from typing import List, Tuple

def has_circular_dependency(dependencies: List[Tuple[str, str]]) -> bool:
    graph = {node: [] for edge in dependencies for node in edge}
    for source, target in dependencies:
        graph[source].append(target)

    def has_cycle(node, visited, stack):
        visited[node] = True
        stack[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if has_cycle(neighbor, visited, stack):
                    return True
            elif stack[neighbor]:
                return True
        stack[node] = False
        return False

    visited = {node: False for node in graph}
    stack = {node: False for node in graph}
    for node in graph:
        if not visited[node]:
            if has_cycle(node, visited, stack):
                return True
    return False