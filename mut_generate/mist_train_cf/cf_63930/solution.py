"""
QUESTION:
Design a function `calculate_diameter(root)` to calculate the diameter of a ternary tree rooted at `root`, where each node is an object with a `data` attribute and a `children` array attribute. The diameter of a tree is the longest path between any two nodes in the tree. Assume the tree is represented using the `Node` class with the structure `class Node: def __init__(self, data): self.data = data; self.children = []`. The function should return the length of the diameter.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

# This function sets 'max_height' and 'node_with_max_height'
def DFS(node, height, max_height, node_with_max_height):
    if not node:
        return
    if height > max_height[0]:
        max_height[0] = height
        node_with_max_height[0] = node
    for child in node.children:
        DFS(child, height + 1, max_height, node_with_max_height)

def calculate_diameter(root):
    if not root:
        return 0
    max_height = [-1]
    node_with_max_height = [None]
    # finding the leftmost node
    DFS(root, 0, max_height, node_with_max_height)
    leftmost_node = node_with_max_height[0]

    # reset max height and node with max height
    max_height = [-1]
    node_with_max_height = [None]
    # finding the rightmost node from leftmost node
    DFS(leftmost_node, 0, max_height, node_with_max_height)
    rightmost_node = node_with_max_height[0]

    # diameter is the distance between leftmost and rightmost node
    diameter = max_height[0]
    return diameter