"""
QUESTION:
Implement the function `load_order(module_dependencies)` that takes a list of module dependencies as input and returns a list of modules in the order they should be loaded to satisfy all dependencies. The input `module_dependencies` is a list of tuples, where each tuple represents a dependency between two modules, with the first element depending on the second element. The function should return any one of the valid load orders if there are multiple possibilities.
"""

def load_order(module_dependencies):
    graph = {}
    for dependency in module_dependencies:
        parent, child = dependency
        if parent not in graph:
            graph[parent] = []
        graph[parent].append(child)

    visited = set()
    load_order_list = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        if node in graph:
            for child in graph[node]:
                dfs(child)
        load_order_list.append(node)

    for module in graph.keys():
        dfs(module)

    return load_order_list[::-1]