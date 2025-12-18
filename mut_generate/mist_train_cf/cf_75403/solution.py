"""
QUESTION:
Implement a function `depth_first_search(root, target_value)` to find a specified node in a ternary tree structure using the depth-first search technique. The ternary tree is represented as a node-based structure where each node has a value and up to three children (left, middle, and right). The function should return the node with the matching `target_value` if found, otherwise return `None`.
"""

class Node:
    def __init__(self, value, left=None, middle=None, right=None):
        self.value = value
        self.left = left
        self.middle = middle
        self.right = right

def depth_first_search(root, target_value):
    # Base case: if the node is None, we have reached an empty branch
    if root is None:
        return None

    # If the current node's value is what we're searching for, return the node
    if root.value == target_value:
        return root

    # Check the left subtree
    found_node = depth_first_search(root.left, target_value)
    if found_node is not None:
        return found_node

    # If not found in left, check the middle subtree
    found_node = depth_first_search(root.middle, target_value)
    if found_node is not None:
        return found_node

    # If not found in left and middle, check the right subtree
    return depth_first_search(root.right, target_value)