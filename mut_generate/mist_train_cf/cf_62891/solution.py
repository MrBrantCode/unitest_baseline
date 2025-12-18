"""
QUESTION:
Find the kth smallest element in an AVL tree using a function named `find_kth_smallest` with the following constraints:

- The function should maintain an O(log n) time complexity where n is the total number of nodes.
- Each node in the AVL tree should have a size field representing the size of its subtree.
- The function should handle edge cases where k is greater than the total number of nodes.
- The AVL tree should be self-balancing and maintain its balance during insertion and deletion operations.
- The function should have a space complexity of O(n) due to the storage of the size field in each node.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = 1
        if left:
            self.size += left.size
        if right:
            self.size += right.size

def find_kth_smallest(root, k):
    """
    This function finds the kth smallest element in an AVL tree.

    Args:
    root (Node): The root of the AVL tree.
    k (int): The position of the element to be found (1-indexed).

    Returns:
    int: The value of the kth smallest element if it exists, otherwise None.
    """
    if not root:
        return None
    if k < 1 or k > root.size:
        return None

    left_size = root.left.size if root.left else 0
    if k == left_size + 1:
        return root.val
    elif k < left_size + 1:
        return find_kth_smallest(root.left, k)
    else:
        return find_kth_smallest(root.right, k - left_size - 1)