"""
QUESTION:
Implement the `max_depth` method for the `Tree` class to return the maximum depth of a binary tree. The method should take no parameters other than the implicit `self` and should return an integer representing the maximum depth. If the tree is empty (`None`), the method should return 0.
"""

def max_depth(tree):
    if tree is None:
        return 0
    else:
        left_depth = max_depth(tree.left) if tree.left else 0
        right_depth = max_depth(tree.right) if tree.right else 0
        return max(left_depth, right_depth) + 1