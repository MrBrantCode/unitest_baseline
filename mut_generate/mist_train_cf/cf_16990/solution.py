"""
QUESTION:
Implement a function `breadthFirstSearch(graph, start, target)` that performs a breadth-first search in a weighted graph to find the shortest path from the `start` vertex to the `target` vertex. The graph should be represented as a dictionary where each key is a vertex and its corresponding value is another dictionary with the neighboring vertices as keys and their respective edge weights as values. The function should return the shortest path as a list of vertices.
"""

def breadthFirstSearch(graph, start, target):
    """
    Performs a breadth-first search in a weighted graph to find the shortest path 
    from the start vertex to the target vertex.

    Args:
    graph (dict): A dictionary representing the graph where each key is a vertex 
                  and its corresponding value is another dictionary with the 
                  neighboring vertices as keys and their respective edge weights 
                  as values.
    start (str): The starting vertex.
    target (str): The target vertex.

    Returns:
    list: The shortest path as a list of vertices. If the target vertex is not 
          found, returns None.
    """
    queue = [start]
    visited = set()
    parent = {start: None}

    while queue:
        current = queue.pop(0)
        if current == target:
            break
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    if target not in parent:
        return None

    path = []
    current = target
    while current is not None:
        path.insert(0, current)
        current = parent[current]

    return path