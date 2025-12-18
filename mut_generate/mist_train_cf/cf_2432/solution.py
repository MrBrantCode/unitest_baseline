"""
QUESTION:
Implement the `depthFirstSearch` function, which performs a depth-first search on a graph using an iterative approach with a stack data structure. The function should take a graph, a start vertex, and an optional target vertex as inputs. If a target vertex is provided, the function should print the path from the start vertex to the target vertex. The function should handle disconnected graphs and have a time complexity of O(V * (V + E)) and a space complexity of O(V^2), where V is the number of vertices in the graph.
"""

def depthFirstSearch(graph, start, target=None):
    stack = [start]
    visited = {start}
    path = {start: [start]}

    while stack:
        vertex = stack.pop()
        if target is not None and vertex == target:
            print(path[vertex])
            return True

        for adjacent_vertex in graph.get(vertex, []):
            if adjacent_vertex not in visited:
                visited.add(adjacent_vertex)
                stack.append(adjacent_vertex)
                path[adjacent_vertex] = path[vertex] + [adjacent_vertex]

    if target is not None:
        return False

    for vertex in graph:
        if vertex not in visited:
            depthFirstSearch(graph, vertex, target)