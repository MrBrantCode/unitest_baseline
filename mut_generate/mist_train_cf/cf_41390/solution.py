"""
QUESTION:
Implement the `print_k_dist_nodes` method for a binary tree, which takes the root of the binary tree and an integer `k` as input and prints all the nodes at distance `k` from the root node. The binary tree node structure is defined as `class TreeNode: def __init__(self, key): self.key = key; self.left = None; self.right = None`.
"""

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def print_k_dist_nodes(root, k):
    if root is None:
        return
    if k == 0:
        print(root.key)
    else:
        print_k_dist_nodes(root.left, k - 1)
        print_k_dist_nodes(root.right, k - 1)