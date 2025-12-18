"""
QUESTION:
Find the inorder successor of a given node in a binary search tree (BST) with parent pointers. The successor of a node `p` is the node with the smallest key greater than `p.val`. Implement the solution without using any additional data structures and without modifying the tree structure. The function should have a time complexity of O(h), where h is the height of the tree.

The function name is `inorderSuccessor(self, node)`, where `node` is the given node in the BST. The function should return the inorder successor of the given node if it exists, otherwise return `null`. Each node in the BST has a parent pointer, left child pointer, and right child pointer. The root node's parent pointer points to `null`. The number of nodes in the tree is in the range `[1, 104]` and all nodes will have unique values.
"""

def inorderSuccessor(self, node):
    if node.right is not None:
        curr = node.right
        while curr.left is not None:
            curr = curr.left
        return curr

    parent = node.parent
    while parent is not None and node == parent.right:
        node = parent
        parent = parent.parent
    return parent