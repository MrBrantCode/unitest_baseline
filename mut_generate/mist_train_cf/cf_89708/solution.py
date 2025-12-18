"""
QUESTION:
Merge two binary trees t1 and t2 into a new binary tree. The merged tree should have a node value equal to the sum of the values of the corresponding nodes in t1 and t2. If a node exists in one tree but not the other, its value should be copied to the merged tree. The function should be able to handle cases where one or both of the input trees are empty.

The merged tree should have a maximum height of log(n), where n is the total number of nodes in the two input trees. It is given that the input trees t1 and t2 are already sorted in descending order based on their values. Implement the function merge_trees(t1, t2) that takes the roots of the two binary trees as input and returns the root of the merged binary tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def merge_trees(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1

    merged_val = t1.val + t2.val
    merged = TreeNode(merged_val)
    merged.left = merge_trees(t1.left, t2.left)
    merged.right = merge_trees(t1.right, t2.right)
    return merged