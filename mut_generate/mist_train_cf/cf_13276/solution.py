"""
QUESTION:
Write a function `findThirdLargest` that takes the root of a Binary Search Tree as input and returns the third largest value in the tree. If the tree has less than three nodes, the function should return `None`. The function should implement its own traversal algorithm without using any built-in data structures or methods.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findThirdLargest(root):
    if root is None or (root.left is None and root.right is None):
        return None

    counter = 3
    current = root
    stack = []

    while True:
        if current is not None:
            stack.append(current)
            current = current.right
        elif stack:
            current = stack.pop()
            counter -= 1
            if counter == 0:
                return current.value
            current = current.left
        else:
            break