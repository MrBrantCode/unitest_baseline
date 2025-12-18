"""
QUESTION:
Write a function `is_d_separated` that takes three nodes X, Y, and Z from a Bayesian network. The function should return `True` if X and Y are d-separated given Z, and `False` otherwise. Assume the Bayesian network is represented as a dictionary where each key is a node and its corresponding value is a list of its neighbors. The function should not use any external libraries.
"""

def is_d_separated(bayesian_network, X, Y, Z):
    """
    Checks if nodes X and Y are d-separated given node Z in a Bayesian network.
    
    Args:
    bayesian_network (dict): A dictionary representing the Bayesian network where each key is a node and its corresponding value is a list of its neighbors.
    X (node): The first node.
    Y (node): The second node.
    Z (node): The node to check for d-separation.
    
    Returns:
    bool: True if X and Y are d-separated given Z, False otherwise.
    """
    
    # Create a set of visited nodes to avoid infinite loops
    visited = set()
    
    # Define a helper function for DFS
    def dfs(current_node, target_node, avoid_node):
        # Add the current node to the visited set
        visited.add(current_node)
        
        # If the current node is the target node, return True
        if current_node == target_node:
            return True
        
        # Iterate over the neighbors of the current node
        for neighbor in bayesian_network.get(current_node, []):
            # Skip the avoid node
            if neighbor == avoid_node or neighbor in visited:
                continue
            
            # Recursively call the dfs function on the neighbor
            if dfs(neighbor, target_node, avoid_node):
                return True
        
        # If no path is found, return False
        return False
    
    # Check all paths from X to Y while avoiding Z
    return not dfs(X, Y, Z)