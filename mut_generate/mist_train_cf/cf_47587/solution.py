"""
QUESTION:
Write a function `pre_order_traversal` that performs a pre-order depth-first traversal on a given n-ary tree using recursion. The function should print the value of each node during traversal. If the tree is empty, it should print "Tree is empty". The tree is represented by a `Node` class with a `value` attribute and a `children` attribute that holds a list of all children nodes.
"""

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

def entrance(node):
    if not node:
        print("Tree is empty")
        return

    print(node.value)
    for child in node.children:
        entrance(child)