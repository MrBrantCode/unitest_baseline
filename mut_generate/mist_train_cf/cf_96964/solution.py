"""
QUESTION:
Implement a function `sum_bst(root)` that calculates the sum of all node values in a given binary search tree (BST) and returns the result modulo 10^9+7. The function should take the root node of the BST as input, where each node has a `val`, `left`, and `right` attribute.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_bst(root):
    sum = [0]
    def inorder_traversal(node):
        if node is not None:
            inorder_traversal(node.left)
            sum[0] += node.val
            inorder_traversal(node.right)
    inorder_traversal(root)
    return sum[0] % (10**9 + 7)