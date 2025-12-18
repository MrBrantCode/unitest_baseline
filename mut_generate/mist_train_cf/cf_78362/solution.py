"""
QUESTION:
Given the root of a binary tree, implement the function `findLonelyNodes(root)` that returns a dictionary where the keys are the values of all lonely nodes in the tree and the values are their respective parent nodes. A lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node. The number of nodes in the tree is in the range [1, 1000] and each node's value is between [1, 10^6].
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findLonelyNodes(root: TreeNode):
    lonely_nodes = {}
    def dfs(node, parent):
        if node:
            # check if the node is a lonely node
            if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
               if node.left is not None:
                   lonely_nodes[node.left.val] = node.val
               else:
                   lonely_nodes[node.right.val] = node.val
              
            dfs(node.left, node)
            dfs(node.right, node)
              
    dfs(root, None)
    return lonely_nodes