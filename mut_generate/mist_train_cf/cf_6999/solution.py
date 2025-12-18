"""
QUESTION:
Implement a function `merge_trees` that merges two binary trees `t1` and `t2` into a new binary tree. The merged tree should have the following properties: 

- The value of a node in the merged tree is the sum of the values of the corresponding nodes in `t1` and `t2`.
- If a node exists in one tree but not in the other, the corresponding node in the merged tree should have the same value as the node in the existing tree.
- If both nodes exist in the original trees, their values should be added together in the merged tree.

Note that the input trees are already sorted in descending order based on their values. The function should return the root of the merged tree.
"""

def merge_trees(t1, t2):
    """
    Merges two binary trees t1 and t2 into a new binary tree.

    The merged tree has the following properties:
    - The value of a node in the merged tree is the sum of the values of the corresponding nodes in t1 and t2.
    - If a node exists in one tree but not in the other, the corresponding node in the merged tree should have the same value as the node in the existing tree.
    - If both nodes exist in the original trees, their values should be added together in the merged tree.

    Args:
        t1 (TreeNode): The root of the first binary tree.
        t2 (TreeNode): The root of the second binary tree.

    Returns:
        TreeNode: The root of the merged binary tree.
    """
    if not t1:
        return t2
    if not t2:
        return t1

    merged_val = t1.val + t2.val
    merged = TreeNode(merged_val)
    merged.left = merge_trees(t1.left, t2.left)
    merged.right = merge_trees(t1.right, t2.right)
    return merged

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right