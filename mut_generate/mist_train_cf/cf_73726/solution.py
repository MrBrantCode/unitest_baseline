"""
QUESTION:
Create a function `Insert` to insert a node into a binary search tree and a function `Search` to search for a node in the binary search tree. The binary search tree node should have an `data` and `left` and `right` children. The tree should maintain the BST property: for any node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The `Insert` function should return the root of the modified tree, and the `Search` function should return a boolean indicating whether the node is found in the tree.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def Insert(root, data):
    if root is None:
        return Node(data)
    elif data <= root.data:
        root.left = Insert(root.left, data)
    else:
        root.right = Insert(root.right, data)
    return root

def Search(root, data):
    while root is not None:
        if data > root.data:
            root = root.right
        elif data < root.data:
            root = root.left
        else:
            return True
    return False