"""
QUESTION:
Write a function `findDeepestNode(root)` that finds the deepest node in a binary tree. The tree is represented by a root node, which contains a value and references to its left and right child nodes. The function should return the value of the deepest node. If multiple deepest nodes exist in the tree, any one of them can be chosen as the result.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findDeepestNode(root):
    deepest = [root.value]
    maxDepth = [0]

    def dfs(node, depth):
        if node is None:
            return
        
        # Update deepest and maxDepth if current depth is greater
        if depth > maxDepth[0]:
            deepest[0] = node.value
            maxDepth[0] = depth
        
        # Traverse left and right subtrees recursively
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    
    dfs(root, 0)
    return deepest[0]