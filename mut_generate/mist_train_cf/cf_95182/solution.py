"""
QUESTION:
Write a function called `calculate_sum` for a binary tree with nodes containing integers. The function should return the sum of all nodes, the maximum value, the minimum value, and the count of nodes that have a value greater than the average value of all nodes in the tree. The binary tree is defined by a root node, and each node has a value and references to its left and right children.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def calculate_sum(root):
    def _calculate_sum_helper(node):
        if node is None:
            return 0, None, None, 0

        left_sum, left_max, left_min, left_count = _calculate_sum_helper(node.left)
        right_sum, right_max, right_min, right_count = _calculate_sum_helper(node.right)

        # Calculate sum
        sum = node.value + left_sum + right_sum

        # Calculate maximum value
        max_val = node.value
        if left_max is not None:
            max_val = max(max_val, left_max)
        if right_max is not None:
            max_val = max(max_val, right_max)

        # Calculate minimum value
        min_val = node.value
        if left_min is not None:
            min_val = min(min_val, left_min)
        if right_min is not None:
            min_val = min(min_val, right_min)

        # Calculate count of nodes greater than average
        count = left_count + right_count
        if node.value > (sum / (left_count + right_count + 1)):
            count += 1

        return sum, max_val, min_val, count

    sum, max_val, min_val, count = _calculate_sum_helper(root)
    return sum, max_val, min_val, count