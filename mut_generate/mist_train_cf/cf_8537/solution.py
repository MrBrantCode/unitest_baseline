"""
QUESTION:
Write a function called `print_reverse_level_order` that takes the root of a binary tree as input and prints all of its elements level by level in reverse order. The function should also return the total number of levels in the tree. The binary tree is defined by nodes where each node has a value and references to its left and right child nodes.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_reverse_level_order(root):
    if root is None:
        return 0

    queue = []
    levels = []

    queue.append(root)

    while len(queue) > 0:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        levels.append(level)

    for i in range(len(levels) - 1, -1, -1):
        print("Level", i, ":", end=" ")
        for j in range(len(levels[i]) - 1, -1, -1):
            print(levels[i][j], end=", ")
        print()

    return len(levels)