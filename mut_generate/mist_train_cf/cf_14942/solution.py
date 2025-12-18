"""
QUESTION:
Write two functions, `level_order_traversal` and `average_of_levels`, to process a binary tree. 

The `level_order_traversal` function should return a list of lists, where each inner list contains the node values of the corresponding level in the binary tree. 

The `average_of_levels` function should return a list of average values, where each value is the average of the node values at the corresponding level in the binary tree.

The functions should handle cases where the input binary tree is empty (i.e., the root is None).
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result

def average_of_levels(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        level_sum = 0
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.pop(0)
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum / level_size)

    return result