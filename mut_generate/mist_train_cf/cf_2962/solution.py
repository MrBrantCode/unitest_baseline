"""
QUESTION:
Write a function `are_mirror_images(root1, root2)` that checks if two binary trees are mirror images of each other. The function should have a time complexity of O(n), where n is the number of nodes in the larger tree, and a space complexity of O(h), where h is the height of the larger tree. The function should return True if the trees are mirror images of each other and False otherwise.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def are_mirror_images(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None or root1.value != root2.value:
        return False
    return are_mirror_images(root1.left, root2.right) and are_mirror_images(root1.right, root2.left)