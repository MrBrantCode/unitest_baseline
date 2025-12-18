"""
QUESTION:
Develop a function named `countLeafNodes` that calculates the number of leaf nodes in a ternary tree. The function should take the root of the ternary tree as an argument. A ternary tree node can have at most three child nodes: left, middle, and right. A leaf node is a node with no child nodes.
"""

class Node:
    def __init__(self, key):
        self.data = key 
        self.left = None
        self.middle = None
        self.right = None

def countLeafNodes(root):
    # if tree is empty
    if root is None:
        return 0 
   
    # if node is leaf node
    if root.left is None and root.middle is None and root.right is None:
        return 1 
       
    # else if node is not a leaf node
    else:
        return countLeafNodes(root.left) + countLeafNodes(root.middle) + countLeafNodes(root.right)