"""
QUESTION:
Design a function called `createNode` that creates a node for a binary tree. The node should have an integer value and pointers to its left and right children, which should be initially set to `None`. Implement this function in Python.

Restrictions: The function should only accept one integer parameter and return a Node object with the specified properties.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def createNode(value):
    """
    Creates a node for a binary tree with the given value.

    Args:
    value (int): The value to be stored in the node.

    Returns:
    Node: A Node object with the specified properties.
    """
    return Node(value)