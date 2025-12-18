"""
QUESTION:
Implement a BinarySearchTree class with the following methods:

- `insert(value)`: Insert a new node with the given value into the binary search tree.
- `search(value)`: Search for a node with the given value in the binary search tree and return the node if found, otherwise return `None`.
- `remove(value)`: Remove the node with the given value from the binary search tree if it exists.

Restrictions: 
- The binary search tree should maintain the property that the value of all the nodes in the left subtree is less than the value of the root, and the value of all the nodes in the right subtree is greater than the value of the root.
- Use a Node class with `value`, `left`, and `right` attributes to represent individual nodes in the binary search tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)

def remove(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = remove(root.left, value)
    elif value > root.value:
        root.right = remove(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.value = temp.value
        root.right = remove(root.right, temp.value)
    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current