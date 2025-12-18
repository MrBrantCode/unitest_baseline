"""
QUESTION:
Implement the `avl_tree_rotation` function, which should perform left and right rotations to balance an AVL tree. The function should handle the four cases of balancing the tree: left-left, left-right, right-left, and right-right. The function should take in a node and the type of rotation as parameters. The function should also handle the update of node heights and child pointers after rotation. The function should have a time complexity of O(1) for the rotation itself, but may involve traversing the tree, resulting in a time complexity of O(log n) for maintaining the AVL property after insertion and deletion operations.
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    if node is None:
        return 0
    return node.height


def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))


def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    update_height(z)
    update_height(y)
    return y


def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    update_height(z)
    update_height(y)
    return y


def avl_tree_rotation(node, type):
    if type == "left-left":
        return right_rotate(node)
    elif type == "left-right":
        node.left = left_rotate(node.left)
        return right_rotate(node)
    elif type == "right-right":
        return left_rotate(node)
    elif type == "right-left":
        node.right = right_rotate(node.right)
        return left_rotate(node)
    else:
        return node