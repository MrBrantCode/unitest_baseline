"""
QUESTION:
Create a function named `search_and_label` that takes a binary tree node and a target value as parameters, and sets a label on each node in the tree that contains the target value. The function should traverse the tree using depth-first search, and assign the label `"MATCH"` to matching nodes. The binary tree node structure should have `value`, `left_child`, `right_child`, and `label` properties.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.label = None

def search_and_label(node, target):
    # Base case: if the node is None (we've reached a leaf), return
    if node is None:
        return

    # If this node's value matches the target, set the label
    if node.value == target:
        node.label = "MATCH"

    # Recursively perform the search on the left and right children
    search_and_label(node.left_child, target)
    search_and_label(node.right_child, target)