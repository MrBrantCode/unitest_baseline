"""
QUESTION:
Design an efficient algorithm for a function named `findKthSmallest(root, k)` to locate the kth smallest element in a balanced AVL tree, with a time complexity of O(log n), where n is the number of nodes. Each node in the AVL tree has an additional attribute `leftCount` to store the size of its left subtree. The function should handle corner cases and unpredictable inputs.
"""

class Node:
    def __init__(self, val, left=None, right=None, leftCount=0):
        self.val = val
        self.left = left
        self.right = right
        self.leftCount = leftCount

def findKthSmallest(root, k):
    """
    This function finds the kth smallest element in a balanced AVL tree.

    Args:
    root (Node): The root node of the AVL tree.
    k (int): The position of the element to find.

    Returns:
    Node: The node containing the kth smallest element.
    """
    
    if root is None: 
        return None
        
    leftCount = root.left.leftCount if root.left else 0

    if leftCount + 1 == k: 
        return root

    if leftCount + 1 < k:
        return findKthSmallest(root.right, k - leftCount - 1)
    else: 
        return findKthSmallest(root.left, k)