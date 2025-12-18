"""
QUESTION:
Design a data structure that allows for fast querying and supports efficient insertion and deletion operations for a large amount of data. Implement an example of this data structure and explain how an incorrect implementation could impact performance and data integrity. Use a B-tree as the chosen data structure and define a function `insert_value` to demonstrate the insertion operation. Ensure the `insert_value` function correctly handles recursion and updates the left or right child of the current node.
"""

class BTreeNode:
    """A node in the B-tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BTree:
    """A B-tree data structure."""
    def __init__(self):
        self.root = None

def insert_value(value, tree):
    """
    Inserts a value into the B-tree.

    Args:
    value (int): The value to insert into the B-tree.
    tree (BTree): The B-tree to insert the value into.

    Returns:
    BTree: The updated B-tree with the inserted value.
    """
    if tree.root is None:
        tree.root = BTreeNode(value)
    else:
        _insert_recursive(value, tree.root)
    return tree

def _insert_recursive(value, node):
    """
    Recursively inserts a value into the B-tree.

    Args:
    value (int): The value to insert into the B-tree.
    node (BTreeNode): The current node in the B-tree.
    """
    if value < node.value:
        if node.left is None:
            node.left = BTreeNode(value)
        else:
            _insert_recursive(value, node.left)
    else:
        if node.right is None:
            node.right = BTreeNode(value)
        else:
            _insert_recursive(value, node.right)