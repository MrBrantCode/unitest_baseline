"""
QUESTION:
Implement a function called `BFS(graph, start, end)` that uses a breadth-first search algorithm to find the shortest path between two nodes `start` and `end` in a graph. The graph is represented as a dictionary where each key is a node and its corresponding value is a list of neighboring nodes. The function should return the shortest path as a list of nodes. If no path is found, the function should return `None`.
"""

def BFS(graph, start, end):
    # Create an empty queue 
    queue = []
    # Create a set to store visited nodes
    visited = set()
    # Enqueue the starting node
    queue.append([start])
    while queue:
        # Get the first path and process it
        path = queue.pop(0)
        # Get the last node from the path
        node = path[-1]
        
        if node == end:
            return path
        elif node not in visited:
            # Create a list of neighbours
            neighbours = graph[node]
            # Go through all neighbours
            for neighbour in neighbours:
                # Create a new path with the neighbour
                new_path = list(path)
                new_path.append(neighbour)
                # Add the new path to the queue
                queue.append(new_path)
            # Mark the node as visited
            visited.add(node)
    return None