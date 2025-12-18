"""
QUESTION:
Write a function called `find_deepest_node` that takes the root of a binary tree as input and returns the value of the deepest node in the tree. If multiple deepest nodes exist, any one of them can be returned. The function should have a time complexity of O(n), where n is the number of nodes in the tree, and a space complexity of O(h), where h is the height of the tree.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_deepest_node(root):
    deepest = None
    maxDepth = -1

    def dfs(node, depth):
        nonlocal deepest, maxDepth

        if node is None:
            return

        if depth > maxDepth:
            maxDepth = depth
            deepest = node.value

        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return deepest