"""
QUESTION:
Implement a function `dfs_traversal` that performs a Depth-First Search (DFS) traversal on a graph. The function should take as input an adjacency list representation of the graph and a source node, and return the order of visited nodes. Assume the graph is represented as a dictionary where each key is a node and its corresponding value is a list of its adjacent nodes.
"""

def dfs_traversal(graph, source):
    """
    Performs a Depth-First Search (DFS) traversal on a graph.

    Args:
    graph (dict): Adjacency list representation of the graph.
    source (node): The source node to start the traversal.

    Returns:
    list: The order of visited nodes.
    """
    
    # Create a set to keep track of visited nodes
    visited = set()
    
    # Create a list to store the order of visited nodes
    traversal_order = []
    
    # Define a helper function for the recursive DFS traversal
    def dfs(node):
        # Mark the current node as visited
        visited.add(node)
        
        # Add the current node to the traversal order
        traversal_order.append(node)
        
        # Iterate over the adjacent nodes of the current node
        for adjacent_node in graph[node]:
            # If the adjacent node has not been visited, perform a recursive DFS traversal
            if adjacent_node not in visited:
                dfs(adjacent_node)
    
    # Perform the DFS traversal starting from the source node
    dfs(source)
    
    # Return the order of visited nodes
    return traversal_order