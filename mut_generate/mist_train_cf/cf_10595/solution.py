"""
QUESTION:
Implement a function named `iterative_tree_traversal` that performs a pre-order traversal on a binary tree using an iterative approach without recursion. The function should take the root node of the binary tree as input and print the node values in the correct order. The binary tree node structure is defined as a class with a `data` attribute and `left` and `right` child attributes. The function should handle the case where the input root node is `None`.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def iterative_tree_traversal(root):
    if root is None:
        return
    
    stack = []
    stack.append(root)
    
    while stack:
        node = stack.pop()
        print(node.data, end=" ")
        
        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)