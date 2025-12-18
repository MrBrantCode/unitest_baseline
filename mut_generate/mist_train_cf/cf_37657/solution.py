"""
QUESTION:
Implement the `breadth_first_search` function, which takes a graph represented as an adjacency list and an initial node as input, and returns the number of nodes expanded during a breadth-first search of the graph. The function should not take any additional parameters.
"""

def breadth_first_search(graph, initial_node):
    queue = [initial_node]
    expanded_nodes = set()
    expanded_nodes.add(initial_node)
    nodes_expanded = 0

    while queue:
        current_node = queue.pop(0)
        nodes_expanded += 1
        for neighbor in graph[current_node]:
            if neighbor not in expanded_nodes:
                expanded_nodes.add(neighbor)
                queue.append(neighbor)

    return nodes_expanded