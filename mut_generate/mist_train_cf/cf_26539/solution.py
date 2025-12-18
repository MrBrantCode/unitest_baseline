"""
QUESTION:
Implement the `breadth_first_search` function to find the shortest path between two nodes in an undirected graph. The function should take in the undirected graph `graph`, a start node `start`, and an end node `end`, and return a list representing the shortest path from the start node to the end node. The graph is connected and there is always a path between the start and end nodes. The `UndirectedGraph` class has methods `add_edge(node1, node2)` and `get_neighbors(node)`, but you can assume these methods are already implemented.
"""

from collections import deque

def shortest_path(graph, start, end):
    queue = deque([start])
    visited = {start: None}

    while queue:
        current_node = queue.popleft()
        if current_node == end:
            break  

        for neighbor in graph.get_neighbors(current_node):
            if neighbor not in visited:
                queue.append(neighbor)
                visited[neighbor] = current_node

    path = [end]
    while path[-1] != start:
        path.append(visited[path[-1]])
    return list(reversed(path))