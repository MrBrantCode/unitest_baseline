"""
QUESTION:
Create a function named `is_identical(tree1, tree2)` that takes two binary search trees as input and returns a boolean value indicating whether the trees are identical or not. The trees can have duplicate values, and each node has attributes `val`, `color` (either "red" or "black"), and `weight` (a positive integer). The function should check if the two trees have the same structure, values, "color" attribute, and "weight" attribute in their nodes.
"""

class TreeNode:
    def __init__(self, val, color, weight):
        self.val = val
        self.color = color
        self.weight = weight
        self.left = None
        self.right = None


def is_identical(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False

    stack1 = []
    stack2 = []

    current1 = tree1
    current2 = tree2

    while stack1 or stack2 or current1 or current2:
        while current1:
            stack1.append(current1)
            current1 = current1.left
        while current2:
            stack2.append(current2)
            current2 = current2.left

        if len(stack1) != len(stack2):
            return False

        if stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if node1.val != node2.val or node1.color != node2.color or node1.weight != node2.weight:
                return False

            current1 = node1.right
            current2 = node2.right

    return True