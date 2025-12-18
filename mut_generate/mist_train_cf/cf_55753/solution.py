"""
QUESTION:
Implement a function named `depth_first_search` that performs a depth-first search on a ternary tree structure to find a node with a specific target value. The function should take two parameters: the current node and the target value. The function should return the node if found, otherwise return None. The ternary tree structure should be defined using a Node class with a value and a list of its children nodes.
"""

class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def depth_first_search(node, target):
    if node.value == target:
        return node
    else:
        for child in node.children:
            found = depth_first_search(child, target)
            if found:
                return found
        return None