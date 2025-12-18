"""
QUESTION:
Implement a function `dfs(tree, start_node)` that performs a depth-first search (DFS) on a tree data structure with the following constraints: the tree can have any number of child nodes for each parent node, the tree can be arbitrarily large, each node in the tree has a unique identifier, and the algorithm should be optimized for memory usage and handle cyclic graphs. The function should start from a specified node and return a list of all visited nodes in the order they were visited. The input tree is represented as a dictionary where the keys are node identifiers and the values are lists of child nodes.
"""

def dfs(tree, start_node):
    visited = set()  # Set to store visited nodes
    stack = [start_node]  # Stack to keep track of nodes to visit
    
    result = []  # List to store the order of visited nodes
    
    while stack:
        node = stack.pop()  # Take the top node from the stack
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            result.append(node)
            
            # Add the child nodes to the stack in reverse order
            for child in reversed(tree[node]):
                stack.append(child)
    
    return result  # Return the list of visited nodes in order