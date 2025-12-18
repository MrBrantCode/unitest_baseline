"""
QUESTION:
Implement the `insert` function to insert keys into a binary search tree and the `create_bst` function to create a binary search tree from a list of keys using the provided `TreeNode` class. The `insert` function should take in the root of the BST and a key to be inserted, returning the root of the modified BST after inserting the key. The `create_bst` function should take in a list of keys and return the root of the created BST. The following restrictions apply: 

- Use the `TreeNode` class with the `__init__` method initializing the `key`, `left`, and `right` attributes.
- Each node in the BST has at most two child nodes (left and right), with the key value of the left child being less than the parent node's key value and the key value of the right child being greater than the parent node's key value.
"""

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root