"""
QUESTION:
Implement the `sortedArrayToBSTRecu` function to construct a height-balanced binary search tree from a given sorted array `nums` within the specified range defined by `start` and `end` indices. The function should return the root of the constructed BST. The `perfect_tree_pivot` function can be used as a helper to find the pivot index for creating a balanced BST. The function should handle edge cases where `start` equals `end`.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def perfect_tree_pivot(n):
    """
    Helper function to find the pivot index for creating a balanced BST
    """
    if n == 0:
        return 0
    m = (n - 1) // 2
    return m

def sortedArrayToBSTRecu(nums, start, end):
    if start == end:
        return None
    mid = start + perfect_tree_pivot(end - start)
    node = TreeNode(nums[mid])
    node.left = sortedArrayToBSTRecu(nums, start, mid)
    node.right = sortedArrayToBSTRecu(nums, mid + 1, end)
    return node