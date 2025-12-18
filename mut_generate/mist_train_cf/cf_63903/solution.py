"""
QUESTION:
Write a function `lca` that finds the lowest common ancestor of two nodes in a binary search tree. The function should take as input the root of the binary search tree and two node values, and return the value of the lowest common ancestor. Assume the binary search tree is represented as a Node class with a `val` attribute and `left_child` and `right_child` attributes. The function should use the properties of a binary search tree to find the lowest common ancestor without storing parent pointers or searching for nodes.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

def lca(root, node1, node2):
    if root.val > max(node1, node2):  
        return lca(root.left_child, node1, node2)
    elif root.val < min(node1, node2):  
        return lca(root.right_child, node1, node2)
    else:
        return root  # if current node is between the two nodes or is one of them it is the LCA
    return root.val