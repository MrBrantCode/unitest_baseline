"""
QUESTION:
Design a function `depth_first_search(node)` that performs a depth-first search on a binary tree and returns the sum of all the nodes in the tree along with the maximum value node found. The binary tree node has three attributes: `value`, `left`, and `right`, representing the value of the node and its left and right children, respectively.
"""

def depth_first_search(node):
    if node is None:
        return 0, float('-inf')
    
    total_sum = node.value
    max_value = node.value
    
    left_sum, left_max = depth_first_search(node.left)
    total_sum += left_sum
    max_value = max(max_value, left_max)
    
    right_sum, right_max = depth_first_search(node.right)
    total_sum += right_sum
    max_value = max(max_value, right_max)
    
    return total_sum, max_value