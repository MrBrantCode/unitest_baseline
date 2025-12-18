"""
QUESTION:
Design a function `print_depth_first_path` to perform a depth-first search on a binary tree and print the path taken for traversing through the tree. The function should take the root node of the binary tree and an optional path parameter (defaulting to an empty list) as input. The function should recursively explore the left and right subtrees of the current node, appending the value of each visited node to the path, and print the path when a leaf node is reached.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key 

def print_depth_first_path(root, path=[]):
    if root is None:
        return
    path.append(root.val)
    if root.left is None and root.right is None:
        print(path)
    else:
        print_depth_first_path(root.left, path.copy())
        print_depth_first_path(root.right, path.copy())