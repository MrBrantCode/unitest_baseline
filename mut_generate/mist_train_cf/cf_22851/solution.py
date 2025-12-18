"""
QUESTION:
Implement a `depth_first_search` function that takes a `target` value as input and returns a boolean indicating whether the value exists in the tree. The tree is represented by a `Node` class with a `value`, a list of `attributes`, and a list of `children`. The function should recursively traverse the tree in a depth-first manner, checking if the `target` value matches the current node's `value`. If a match is found, return `True`. If all nodes are traversed without finding a match, return `False`.
"""

class Node:
    def __init__(self, value, attributes=None):
        self.value = value
        self.attributes = attributes
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def depth_first_search(node, target):
    if node.value == target:
        return True

    for child in node.children:
        if depth_first_search(child, target):
            return True

    return False