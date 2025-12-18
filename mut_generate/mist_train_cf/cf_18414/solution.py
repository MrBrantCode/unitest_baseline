"""
QUESTION:
Write a function `find_common_ancestor(root, node1, node2)` that finds the first common ancestor of two nodes `node1` and `node2` in a binary search tree `root`. The function should have a time complexity of O(log n), where n is the number of nodes in the tree. The binary search tree is ordered, meaning all nodes to the left of a node have values less than the node's value, and all nodes to the right of a node have values greater than the node's value.
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