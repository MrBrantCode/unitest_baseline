"""
QUESTION:
Create a function called `is_identical` that checks if two binary trees are identical. The function should take two binary tree roots, `root1` and `root2`, as input and return a boolean value indicating whether the trees are identical or not. The function should consider two trees identical if they have the same structure and all corresponding nodes have the same data. The binary tree nodes are assumed to have `data`, `left`, and `right` attributes.
"""

def is_identical(root1, root2):
    """
    Checks if two binary trees are identical.

    Args:
    root1 (Node): The root of the first binary tree.
    root2 (Node): The root of the second binary tree.

    Returns:
    bool: True if the trees are identical, False otherwise.
    """
    # Check if both trees are empty
    if root1 is None and root2 is None:
        return True
    
    # Check if one tree is empty and the other is not
    if root1 is None or root2 is None:
        return False
    
    # Check if the data of the current nodes is the same
    if root1.data == root2.data:
        # Recursively check if the left and right subtrees are identical
        left_identical = is_identical(root1.left, root2.left)
        right_identical = is_identical(root1.right, root2.right)
        # Return True if both subtrees are identical
        return left_identical and right_identical
    
    # If none of the above conditions are met, the trees are not identical
    return False