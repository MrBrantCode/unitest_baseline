"""
QUESTION:
Write a recursive function `sum_and_max` that calculates the sum of all nodes and finds the maximum value in a binary tree. The function should have a time complexity of O(n), where n is the number of nodes, and use constant space, without extra data structures to store intermediate results. The function should return a tuple containing the sum of all nodes and the maximum value among all nodes.
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def sum_and_max(root):
    if root is None:
        return 0, float('-inf')
    
    left_sum, left_max = sum_and_max(root.left)
    right_sum, right_max = sum_and_max(root.right)
    
    total_sum = root.val + left_sum + right_sum
    max_value = max(root.val, left_max, right_max)
    
    return total_sum, max_value