"""
QUESTION:
Implement a function named `bst_traversal` that performs binary search tree traversal in preorder, inorder, and postorder. Define the function without considering the actual tree creation. It should take a node as input and print the node values in the respective traversal orders.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bst_traversal(node):
    """
    Performs binary search tree traversal in preorder, inorder, and postorder.
    
    Args:
    node (TreeNode): The root node of the binary search tree.
    
    Returns:
    tuple: A tuple containing lists of node values in preorder, inorder, and postorder traversal orders.
    """

    # Initialize empty lists to store node values in different traversal orders
    preorder = []
    inorder = []
    postorder = []

    # Define helper functions for each traversal type
    def preorder_traversal(node):
        if node:
            preorder.append(node.value)  # Visit the current node
            preorder_traversal(node.left)  # Traverse the left subtree
            preorder_traversal(node.right)  # Traverse the right subtree

    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)  # Traverse the left subtree
            inorder.append(node.value)  # Visit the current node
            inorder_traversal(node.right)  # Traverse the right subtree

    def postorder_traversal(node):
        if node:
            postorder_traversal(node.left)  # Traverse the left subtree
            postorder_traversal(node.right)  # Traverse the right subtree
            postorder.append(node.value)  # Visit the current node

    # Perform traversals
    preorder_traversal(node)
    inorder_traversal(node)
    postorder_traversal(node)

    # Return the traversal orders
    return preorder, inorder, postorder