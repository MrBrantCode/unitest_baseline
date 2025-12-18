"""
QUESTION:
Implement a function called `balanceBST(root)` that takes the root of a binary search tree as input and returns the root of a balanced binary search tree with the same node values. The balanceBST function should work such that for any given binary search tree, the depth of the two subtrees of every node in the resulting balanced tree never differ by more than 1.

Additionally, implement functions to add a new node and delete a node from the balanced binary search tree, ensuring that the tree remains balanced after each operation. 

The input tree contains between 1 and 10^4 nodes, each with distinct values between 1 and 10^5.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balanceBST(root):
    nodes = []
    def inorderTraversal(node):
        if node is None:
            return
        inorderTraversal(node.left)
        nodes.append(node)
        inorderTraversal(node.right)
    
    def sortedArrayToBST(nodes, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        node = nodes[mid]
        node.left = sortedArrayToBST(nodes, start, mid - 1)
        node.right = sortedArrayToBST(nodes, mid + 1, end)
        return node
    
    inorderTraversal(root)
    return sortedArrayToBST(nodes, 0, len(nodes) - 1)