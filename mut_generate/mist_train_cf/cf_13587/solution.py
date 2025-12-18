"""
QUESTION:
Create a function called `print_preorder(root)` that prints the contents of a binary tree in pre-order format. The function should handle cases where the binary tree is empty (`root` is `None`) or contains invalid values (not an instance of the `Node` class). The function should take one argument `root`, which is the root node of the binary tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_preorder(root):
    # Handle case where the tree is empty
    if root is None:
        return

    # Handle case where the tree contains invalid values
    if not isinstance(root, Node):
        print("Invalid binary tree")
        return

    # Print the value of the current node
    print(root.value, end=" ")

    # Traverse the left subtree in pre-order
    print_preorder(root.left)

    # Traverse the right subtree in pre-order
    print_preorder(root.right)