"""
QUESTION:
Design a function `isIdentical(root1, root2)` to check if two given binary trees rooted at `root1` and `root2` are identical. Each node in the binary tree contains an integer value, a character value, and a timestamp value. The function should compare the integer, character, and timestamp values of the corresponding nodes and return true only if all values are identical in both trees. The time complexity of the function should be O(n) and the space complexity should be O(log n), where n is the number of nodes in the larger tree.
"""

class Node:
    def __init__(self, integer, character, timestamp):
        self.integer = integer
        self.character = character
        self.timestamp = timestamp
        self.left = None
        self.right = None

def entrance(root1, root2):
    # Base Case
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    # Check if values of root1 and root2 are identical
    if root1.integer != root2.integer or root1.character != root2.character or root1.timestamp != root2.timestamp:
        return False

    # Recursively check left and right subtrees
    return entrance(root1.left, root2.left) and entrance(root1.right, root2.right)