"""
QUESTION:
Calculate the height of a strictly binary tree where every non-leaf node has two children and there's a positive constant restricting the ratio of the lengths of any two root-to-leaf paths. Define the height `h` of such a tree given `N`, the quantity of nodes in the tree, where `N` is more than one. The tree's node count `N` should be in the form of `2^n - 1`, where `n` is a positive integer.
"""

import math

def h(N):
    """Calculate the height of a binary tree"""
    # Check if N is greater than 1
    if N <= 1:
        return "N should be more than 1"
    
    # Calculate height
    height = math.log(N + 1, 2)
    
    # Return the calculated height
    return int(height)