"""
QUESTION:
Implement a function `find_lonely_nodes` that takes a binary tree root node as input and returns a list of integers representing the values of all "lonely" nodes in the tree, where a node is considered "lonely" if it has no siblings.
"""

from typing import List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_lonely_nodes(root: TreeNode) -> List[int]:
    lonely_nodes = []

    def dfs(node, is_lonely):
        if node is None:
            return
        if is_lonely:
            lonely_nodes.append(node.value)
        is_lonely = (node.left is None) ^ (node.right is None)
        dfs(node.left, is_lonely)
        dfs(node.right, is_lonely)

    dfs(root, False)
    return lonely_nodes