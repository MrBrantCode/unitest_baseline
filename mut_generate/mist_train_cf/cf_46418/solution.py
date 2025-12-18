"""
QUESTION:
Convert a sorted array into a height-balanced binary search tree where each node stores the sum of all elements in its subtree.

The input is a sorted array `nums` of integers, where `1 <= len(nums) <= 10^4` and `-10^4 <= nums[i] <= 10^4`. The output is the root node of the height-balanced binary search tree. The tree should be height-balanced, meaning the depth of the two subtrees of every node never differs by more than one. Each node should store the sum of all elements in its subtree.

Implement the `sortedArrayToBST` function to solve this problem.
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.size = 0

def sortedArrayToBST(nums, lo = None, hi = None):
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(nums) - 1
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    node = Node(sum(nums[lo:hi+1])) # Node's val stores sum of elements in its subtree
    node.size = hi-lo+1
    node.left = sortedArrayToBST(nums, lo, mid - 1)
    node.right = sortedArrayToBST(nums, mid + 1, hi)
    return node