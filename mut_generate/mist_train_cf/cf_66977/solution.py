"""
QUESTION:
Write a function `diameter_and_sum` that takes a binary tree node as input and returns the diameter of the binary tree (the length of the longest path between any two nodes) and the sum of integers along the longest path. The function should consider negative or zero values in the nodes and handle edge cases such as unstable states and rapid tree modifications. The function should be optimized for execution speed and handle large binary trees of up to 10^6 nodes. If competing paths have equal lengths, the function should return the one with the highest sum.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def diameter_and_sum(root):
    def helper(root):
        if root is None:
            return 0, 0, 0, 0
        left_diam, left_height, left_sum, left_path_sum = helper(root.left)
        right_diam, right_height, right_sum, right_path_sum = helper(root.right)

        current_diam = left_height + right_height + 1
        current_sum = left_sum + right_sum + root.value
        current_path_sum = max(left_path_sum, right_path_sum, left_sum + right_sum + root.value)
        
        return max(left_diam, right_diam, current_diam), max(left_height, right_height) + 1, current_sum, current_path_sum

    diam, _, _, path_sum = helper(root)
    return diam, path_sum