"""
QUESTION:
Implement a function `construct_tree` that takes a list of integers and `None` as input and constructs a binary tree based on the given level-order traversal. The function should return the root node of the constructed binary tree. The binary tree is defined by the `TreeNode` class with the structure `class TreeNode: def __init__(self, val=0, left=None, right=None): self.val = val; self.left = left; self.right = right`. The input list is guaranteed to be non-empty.
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while i < len(nodes):
        current = queue.pop(0)

        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)

        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)

        i += 1

    return root