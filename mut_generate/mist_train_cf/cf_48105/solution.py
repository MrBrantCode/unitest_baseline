"""
QUESTION:
Write a function `shortest_path(graph, start, end)` to find the shortest path between two nodes in a weighted graph. The graph is represented as a dictionary where the keys are the node names and the values are dictionaries representing the neighboring nodes and their corresponding edge weights. The function should return the shortest path from the `start` node to the `end` node. The graph is guaranteed to have non-negative edge weights.
"""

from queue import PriorityQueue

def shortest_path(graph, start, end):
    """
    This function finds the shortest path between two nodes in a weighted graph.

    Args:
    graph (dict): A dictionary representing the graph, where each key is a node and its corresponding value is another dictionary.
                  The inner dictionary's keys are the neighboring nodes and its values are the edge weights.
    start (node): The starting node for the shortest path.
    end (node): The ending node for the shortest path.

    Returns:
    list: A list of nodes representing the shortest path from the start node to the end node.
    """
    
    # Initialize a priority queue to keep track of nodes to visit, with their distances from the start node
    queue = PriorityQueue()
    queue.put((0, start))
    
    # Initialize a dictionary to store the shortest distance to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Initialize a dictionary to store the previous node in the shortest path
    previous_nodes = {node: None for node in graph}
    
    # Continue visiting nodes until the queue is empty
    while not queue.empty():
        (dist, current_node) = queue.get()
        # If the current distance is not the shortest known distance, skip this node
        if dist != distances[current_node]:
            continue
        
        # For each neighbor of the current node
        for neighbor, neighbor_dist in graph[current_node].items():
            # Calculate the new distance to the neighbor
            old_dist = distances[neighbor]
            new_dist = distances[current_node] + neighbor_dist
            
            # If the new distance is shorter, update the shortest distance and previous node
            if new_dist < old_dist:
                distances[neighbor] = new_dist
                previous_nodes[neighbor] = current_node
                queue.put((new_dist, neighbor))
    
    # Reconstruct the shortest path by following the chain of previous nodes
    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    
    # Return the shortest path in the correct order
    path.reverse()
    
    return path