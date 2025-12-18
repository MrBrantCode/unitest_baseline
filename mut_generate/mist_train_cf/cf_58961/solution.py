"""
QUESTION:
Given a binary tree node represented as a dictionary with keys 'data', 'left', and 'right', write a function `inRange(node, minVal, maxVal)` that returns a tuple containing the count of terminal nodes (leaf nodes) within the given range `[minVal, maxVal]` and the sum of their values. A node is considered within the range if its value is greater than or equal to `minVal` and less than or equal to `maxVal`.
"""

def entrance(node, minVal, maxVal):
    # Base case: when the node is None
    if node is None:
        return (0, 0)
    
    # Recursive calls for left and right subtrees
    left = entrance(node.get('left'), minVal, maxVal)
    right = entrance(node.get('right'), minVal, maxVal)

    # If the node is a leaf (has no children) and its value is within the range
    if not node.get('left') and not node.get('right') and minVal <= node['data'] <= maxVal:
        return (left[0] + right[0] + 1, left[1] + right[1] + node['data'])
    
    # If the node is not a leaf or its value is not within the range
    return (left[0] + right[0], left[1] + right[1])