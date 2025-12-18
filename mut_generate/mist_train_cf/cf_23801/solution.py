"""
QUESTION:
Create a function called `array_to_binary_tree` that takes a list of integers as input and constructs a binary tree where the input list represents the pre-order traversal of the binary tree. The function should return the root node of the constructed binary tree.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def array_to_binary_tree(arr):
    """
    This function constructs a binary tree from a given list of integers.
    The input list represents the pre-order traversal of the binary tree.
    
    Parameters:
    arr (list): A list of integers representing the pre-order traversal of the binary tree.
    
    Returns:
    TreeNode: The root node of the constructed binary tree.
    """
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        current_node = queue.pop(0)
        if i < len(arr):
            current_node.left = TreeNode(arr[i])
            queue.append(current_node.left)
            i += 1
        if i < len(arr):
            current_node.right = TreeNode(arr[i])
            queue.append(current_node.right)
            i += 1
    return root