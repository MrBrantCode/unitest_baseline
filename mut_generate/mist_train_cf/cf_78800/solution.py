"""
QUESTION:
Design a function `maxDepth` that calculates the maximum depth of a binary tree, and a function `depthFirstTraversal` that performs a depth-first traversal on the binary tree. The `depthFirstTraversal` function should take a function `visit` as a parameter, which will be applied to the data of each node during the traversal. The binary tree is represented by a Node class with `data`, `left`, and `right` attributes. The functions should be able to handle trees with up to 1 million nodes. The `depthFirstTraversal` function should perform a preorder traversal (Root, Left, Right).
"""

class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None 

def maxDepth(node): 
    if node is None: 
        return 0   
    else : 
        leftDepth = maxDepth(node.left) 
        rightDepth = maxDepth(node.right) 
        if (leftDepth > rightDepth): 
            return leftDepth+1
        else: 
            return rightDepth+1

def depthFirstTraversal(node, visit): 
    if node: 
        visit(node.data),
        depthFirstTraversal(node.left, visit) 
        depthFirstTraversal(node.right, visit)