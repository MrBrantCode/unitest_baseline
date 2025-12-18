"""
QUESTION:
Create a function `cloneTree(node)` that clones a binary tree with random pointers. The function takes the root node of the original binary tree as input, and returns the root node of the cloned binary tree.

The binary tree node is defined as a class with four attributes: `val` (an integer), `left` (the left child node), `right` (the right child node), and `random` (a random pointer to any node in the tree or `None`).

The cloned binary tree should have the same structure as the original tree, with each node having the same value as its corresponding node in the original tree. The `left`, `right`, and `random` pointers of the cloned nodes should point to the corresponding cloned nodes.

Constraints: `0 <= d <= 1000`, where `d` is the depth of the binary tree, and `-10000 <= Node.val <= 10000`.
"""

class Node:
    def __init__(self, x: int, left: 'Node' = None, right: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.left = left
        self.right = right
        self.random = random

def cloneTree(node: 'Node') -> 'Node':
    lookup = {}
    def dfs(node):
        if not node: return None
        if node in lookup: return lookup[node]
        clone = Node(node.val)
        lookup[node] = clone
        clone.left = dfs(node.left)
        clone.right = dfs(node.right)
        clone.random = dfs(node.random)
        return clone
    return dfs(node)