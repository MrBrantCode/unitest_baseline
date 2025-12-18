"""
QUESTION:
Implement a function `find_size(root)` to find the size of a binary tree, where each node has a parent pointer in addition to left and right child pointers. The function should take the root of the binary tree as input and return the total number of nodes in the tree.
"""

def find_size(root):
    if root is None:
        return 0
    
    # Initialize the size to 1 for the root node
    size = 1
    
    # Recursively find the size of the left subtree
    size += find_size(root.left)
    
    # Recursively find the size of the right subtree
    size += find_size(root.right)
    
    return size