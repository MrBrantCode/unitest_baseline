"""
QUESTION:
Implement a function named `BFS` that performs a Breadth-First Search traversal between two nodes in a graph to find the shortest path. The function should take three parameters: `graph`, `start_node`, and `end_node`. The function should return the shortest path from `start_node` to `end_node` if it exists, or `None` if no path exists. The graph can be directed or undirected, but it is unweighted. The function should use a queue data structure and a set to keep track of visited nodes.
"""

from collections import deque

def BFS(graph, start_node, end_node):
    """
    Performs a Breadth-First Search traversal between two nodes in a graph to find the shortest path.
    
    Args:
        graph (dict): A dictionary representing the graph, where each key is a node and its corresponding value is a list of its neighbors.
        start_node (any): The node to start the search from.
        end_node (any): The node to search for.
    
    Returns:
        list: The shortest path from start_node to end_node if it exists, otherwise None.
    """
    
    # Create a queue for BFS, enqueue the start node
    queue = deque([[start_node]])
    
    # Create a set to keep track of visited nodes
    visited = set()
    
    # Perform BFS
    while queue:
        # Dequeue the first path in the queue
        path = queue.popleft()
        
        # Get the last node in the path
        node = path[-1]
        
        # If the node is not visited
        if node not in visited:
            # Mark the node as visited
            visited.add(node)
            
            # If the node is the end node, return the path
            if node == end_node:
                return path
            
            # For each neighbor of the node that has not been visited
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    # Create a new path by appending the neighbor to the current path
                    new_path = list(path)
                    new_path.append(neighbor)
                    # Enqueue the new path
                    queue.append(new_path)
    
    # If the end node is not reachable from the start node, return None
    return None