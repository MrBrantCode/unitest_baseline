"""
QUESTION:
Design a function `print_spiral(root)` that prints the elements of a binary tree in spiral order and records the level of each node. The function should take the root of the binary tree as input and minimize its time complexity. The binary tree nodes are defined with a value and optional left and right children.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def entrance(root):
    if root is None:
        return 

    # Create two stacks to hold the current level and the next level
    current_level = []
    next_level = []

    # Add the root node to the current level's stack and initialize level to 0
    current_level.append(root)
    level = 0

    # Repeatedly process until both of the stacks are empty
    while current_level:
        # Pop a node from the current level stack and print it along with its level
        node = current_level.pop()
        print('value:', node.val, "level:", level)

        # Prepare for the next level
        if level % 2 == 0:  # For even levels, add left before right.
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        else:  # For odd levels, add right before left.
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)

        # If the current level stack is empty, move to the next level
        if not current_level:
            current_level, next_level = next_level, current_level
            level += 1