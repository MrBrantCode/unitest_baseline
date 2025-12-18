"""
QUESTION:
Given a binary tree, implement a function `sum_and_count_evens` that returns a tuple containing the sum of all numbers in the tree and the total number of even numbers in the tree. The binary tree node is represented as a class with an integer value, and optional left and right child nodes. The function should be able to handle an empty tree (i.e., `root` is `None`).
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sum_and_count_evens(root):
    if root is None:  
        return 0, 0

    left_sum, left_evens = sum_and_count_evens(root.left)    
    right_sum, right_evens = sum_and_count_evens(root.right)  

    total = left_sum + right_sum + root.val  
    evens = left_evens + right_evens  

    if root.val % 2 == 0:  
        evens += 1

    return total, evens