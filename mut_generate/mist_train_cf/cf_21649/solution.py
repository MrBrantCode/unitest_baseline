"""
QUESTION:
Create a function named `print_odd_paths` that takes the root of a binary tree as input and prints all paths from a leaf node to another leaf node with an odd number of nodes, where the maximum path length does not exceed 10 nodes.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_odd_paths(root):
    def is_leaf(node):
        return node.left is None and node.right is None
    
    def print_path(path):
        if len(path) % 2 == 1 and len(path) <= 10:
            print(" -> ".join(str(node.value) for node in path))
    
    def traverse(node, path):
        if node is None:
            return
        
        path.append(node)
        
        if is_leaf(node):
            print_path(path)
        
        traverse(node.left, path)
        traverse(node.right, path)
        
        path.pop()
    
    traverse(root, [])