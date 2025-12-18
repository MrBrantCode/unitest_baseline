"""
QUESTION:
Given the root of a symmetric binary search tree, implement two functions: `diameter` and `isSymmetric`. The `diameter` function should calculate the diameter of the tree with a time complexity of O(log N) assuming the tree remains balanced after insertion. The `isSymmetric` function should verify if the tree remains symmetric after the insertion of a new node. If the symmetry is disrupted, the tree should be adjusted to restore its balance.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def entance(root):
    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def isMirror(node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False

        return (node1.val == node2.val) and isMirror(node1.right, node2.left) and isMirror(node1.left, node2.right)

    diameter = 2 * max(height(root.left), height(root.right))
    is_symmetric = isMirror(root.left, root.right)
    return diameter, is_symmetric