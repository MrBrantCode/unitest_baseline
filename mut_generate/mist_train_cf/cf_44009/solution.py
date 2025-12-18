"""
QUESTION:
Implement a function `search(root, key)` that performs a Depth-First search traversal on a binary search tree to find a specific node with a given key. The function should take two parameters: `root` (the root node of the binary search tree) and `key` (the value of the node to be searched). The function should return the node with the matching key if found, or `None` otherwise.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def search(root, key):
    if root is None or root.val == key: 
      return root
 
    if root.val < key: 
      return search(root.right,key) 
    
    return search(root.left,key)