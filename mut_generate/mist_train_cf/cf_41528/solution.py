"""
QUESTION:
Implement a function `is_inline(node, config)` that checks if a given node is in line with a specified configuration. 

The function takes two parameters: `node` (a point in a 2D coordinate system that can be None) and `config` (a list of two points representing a line in the 2D coordinate system). 

The function should return True if the node is in line with the configuration, and False otherwise. If the node is None, the function should return False.
"""

def is_inline(node, config):
    if node is None:
        return False
    x, y = node
    x1, y1 = config[0]
    x2, y2 = config[1]
    return (y - y1) * (x2 - x1) == (y2 - y1) * (x - x1)