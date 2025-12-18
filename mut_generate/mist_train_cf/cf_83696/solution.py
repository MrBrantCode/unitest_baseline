"""
QUESTION:
Implement a function `zigzag_traversal(root)` that performs a level-wise zig-zag traversal on a binary or n-ary tree. The traversal should alternate between left-to-right and right-to-left at each depth level. The function should return a list of node values in the order they are visited. The tree is represented by a Node class where each node has a value and a list of children. The function should be efficient in terms of time and space complexity.
"""

from collections import deque

class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children if children is not None else []

def zigzag_traversal(root):
    if not root:
        return []

    result, current_level, next_level, left_to_right = [], deque([root]), deque(), True

    while current_level:
        node = current_level.pop()
        result.append(node.val)

        if left_to_right:
            next_level.extend(reversed(node.children))
        else:
            next_level.extend(node.children)

        if not current_level:
            current_level, next_level = next_level, deque()
            left_to_right = not left_to_right

    return result