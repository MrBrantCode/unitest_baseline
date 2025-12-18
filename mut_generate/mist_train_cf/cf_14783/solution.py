"""
QUESTION:
Implement a function `dfs(root, target)` that performs a depth-first search on a tree to find a given target value. The tree is represented as a collection of nodes, where each node has a value and a list of child nodes. The function should return the node with the target value if found, or `None` otherwise.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def dfs(root, target):
    stack = [root]

    while stack:
        node = stack.pop()

        if node.value == target:
            return node

        for child in reversed(node.children):
            stack.append(child)

    return None