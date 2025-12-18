"""
QUESTION:
Write a function `minDiffInBST` that takes the root of a binary search tree (BST) as input and returns the minimum absolute difference between values of any two nodes in the tree. The BST has distinct nodes and at least 2 nodes. The function should consider the absolute difference between any two nodes, not just adjacent nodes in the tree, but the nodes are distinct, so checking for the smallest difference between consecutive in-order traversal values will suffice.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDiffInBST(root):
    def inorder_traversal(node, result):
        if node:
            inorder_traversal(node.left, result)
            result.append(node.val)
            inorder_traversal(node.right, result)

    values = []
    inorder_traversal(root, values)
    min_diff = float('inf')
    for i in range(1, len(values)):
        min_diff = min(min_diff, values[i] - values[i-1])
    return min_diff