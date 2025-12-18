"""
QUESTION:
Find the function `find_common_ancestor(root, node1, node2)` that returns the first common ancestor of two nodes in a binary search tree. The binary search tree is sorted in ascending order, where for each node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The function should have a time complexity of O(log n), where n is the number of nodes in the tree.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_common_ancestor(root, node1, node2):
    if root is None:
        return None
    
    if root.value == node1.value or root.value == node2.value:
        return root
    
    if root.value > node1.value and root.value > node2.value:
        return find_common_ancestor(root.left, node1, node2)
    
    if root.value < node1.value and root.value < node2.value:
        return find_common_ancestor(root.right, node1, node2)
    
    return root