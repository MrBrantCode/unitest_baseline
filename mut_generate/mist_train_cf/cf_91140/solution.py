"""
QUESTION:
Construct a function `constructBST` that constructs a balanced binary search tree (BST) from a given list of unique integers. The function should take a list of integers as input and return the root node of the constructed BST. The resulting tree should be height balanced and have the minimum possible height. The input list may be unsorted and may contain duplicate values, but the constructed BST should only contain unique values in ascending order.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def constructBST(nums):
    def constructHelper(nums, left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = constructHelper(nums, left, mid - 1)
        root.right = constructHelper(nums, mid + 1, right)
        return root
    
    nums = sorted(set(nums))  # Remove duplicates and sort the list
    return constructHelper(nums, 0, len(nums) - 1)