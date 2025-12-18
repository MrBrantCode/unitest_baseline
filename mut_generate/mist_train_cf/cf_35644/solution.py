"""
QUESTION:
Write a function `resolve_dependencies(initial, dependencies)` that resolves dependencies for a given package based on the provided dependency list. The function takes in a boolean flag `initial` indicating whether the current package is the initial package being installed, and a list of tuples `dependencies` representing dependencies between packages. Each tuple consists of two strings: the name of the dependent package and the name of the dependency package. The function should return a list of package names representing a valid installation order. If there are multiple valid installation orders, return any one of them.
"""

def resolve_dependencies(initial, dependencies):
    graph = {}
    for dep in dependencies:
        if dep[0] not in graph:
            graph[dep[0]] = []
        graph[dep[0]].append(dep[1])

    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        if node in graph:
            for neighbor in graph[node]:
                dfs(neighbor)
        result.append(node)

    if initial:
        for package in graph.keys():
            dfs(package)
    else:
        for package in graph.keys():
            if package not in visited:
                dfs(package)

    return result[::-1]