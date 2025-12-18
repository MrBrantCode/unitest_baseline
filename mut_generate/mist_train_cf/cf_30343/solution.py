"""
QUESTION:
Implement a function `find_max_clique` that takes a graph represented as an adjacency list as input and populates a `Solution` object with the maximum clique size, number of edges, and the assignment of vertices to the maximum clique. The `Solution` object has attributes `max_clique_size`, `number_of_edges`, and `assignment`. The function should find the maximum clique size by identifying the largest subset of vertices where every two distinct vertices are adjacent, and calculate the number of edges as the count of unique pairs of vertices connected by an edge. The function should also store the assignment of vertices to the maximum clique found.
"""

def find_max_clique(graph):
    def is_clique(candidate, graph):
        for i in range(len(candidate)):
            for j in range(i + 1, len(candidate)):
                if candidate[j] not in graph[candidate[i]]:
                    return False
        return True

    def expand(candidate, remaining, graph, max_clique_size, assignment):
        if not remaining and len(candidate) > max_clique_size[0]:
            if is_clique(candidate, graph):
                max_clique_size[0] = len(candidate)
                assignment.clear()
                assignment.extend(candidate)
        for node in remaining:
            new_candidate = candidate + [node]
            new_remaining = [n for n in remaining if n in graph[node]]
            expand(new_candidate, new_remaining, graph, max_clique_size, assignment)

    max_clique_size = [0]
    assignment = []
    nodes = list(graph.keys())
    expand([], nodes, graph, max_clique_size, assignment)

    number_of_edges = sum(len(neighbors) for neighbors in graph.values()) // 2
    return {
        'max_clique_size': max_clique_size[0],
        'number_of_edges': number_of_edges,
        'assignment': assignment
    }