"""
QUESTION:
Create a function `print_odd_paths` that takes the root of a binary tree as input and prints all paths from the root to a leaf node that have an odd number of nodes and do not exceed 10 nodes in length. The function should consider each path as a sequence of node values, starting and ending at a leaf node, and print the node values in the path separated by " -> ".
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