"""
QUESTION:
Write a function called `maxDepth` that takes the root of a binary tree as input and returns a tuple containing the maximum depth of the tree and the path from the root to the node with the maximum depth. Assume that the binary tree is represented using a Node class with a value and optional left and right children. The function should be able to handle edge cases, including unbalanced trees, and should have a time complexity of O(N), where N is the number of nodes in the tree.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    def dfs(node, depth, path):
        if not node:
            return depth-1, path
        if not node.left and not node.right:
            return depth, path + [node.val]
        
        leftDepth, leftPath = dfs(node.left, depth+1, path + [node.val])
        rightDepth, rightPath = dfs(node.right, depth+1, path + [node.val])
        
        if leftDepth > rightDepth:
            return leftDepth, leftPath
        else:
            return rightDepth, rightPath
    
    max_depth, max_path = dfs(root, 1, [])
    return max_depth, max_path