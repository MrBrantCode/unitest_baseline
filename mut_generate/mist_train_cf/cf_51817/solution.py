"""
QUESTION:
Implement a function named `findSmallestAndLargest` that takes the root of a binary search tree as input and returns a tuple containing the smallest and largest values in the tree. The function should have a time complexity of O(h), where h is the height of the tree, and should be optimized to handle trees with up to 10^5 nodes. The function can assume that the input tree is a properly constructed binary search tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findSmallestAndLargest(root):
    """
    This function finds the smallest and largest values in a binary search tree.

    Args:
    root: The root node of the binary search tree.

    Returns:
    A tuple containing the smallest and largest values in the tree.
    """
    
    # Function to find the smallest value in the tree
    def find_min(node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    # Function to find the largest value in the tree
    def find_max(node):
        current = node
        while current.right is not None:
            current = current.right
        return current.value

    if root is None:
        return None

    smallest = find_min(root)
    largest = find_max(root)

    return (smallest, largest)