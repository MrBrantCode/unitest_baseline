"""
QUESTION:
Create a function `create_inverted_binary_tree` that takes a list of integers as input and returns the root of an inverted binary tree, where each level consists of the input integers in sequence. The tree structure should be defined such that the root is at the lowest layer, and each node's left child corresponds to the next layer, while its right child is on the same layer, with new integers taking precedence over old ones. Additionally, implement a breadth-first traversal method to validate the ordered sequence. The function should handle empty input lists by returning `None`.
"""

from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_inverted_binary_tree(arr):
    if len(arr) == 0:
        return None

    root = Node(arr[0])
    current_nodes = deque([root])

    for val in arr[1:]:
        node = Node(val)
        current_node = current_nodes[0]

        if current_node.left is None:
            current_node.left = node
        else:
            current_node.right = node
            current_nodes.popleft()

        current_nodes.append(node)

    return root