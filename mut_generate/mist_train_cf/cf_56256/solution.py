"""
QUESTION:
Write a function `getHeight(root)` and `insert(root, key)` to identify the height of an AVL tree and balance the tree if it becomes unbalanced after inserting a new node, respectively. The `getHeight(root)` function should return the height of the AVL tree, and the `insert(root, key)` function should return the new root of the balanced tree after insertion. The tree should be balanced according to the AVL tree balance condition: for every node, the absolute difference between the heights of its left and right subtrees should not exceed 1.
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def getHeight(root):
    if not root:
        return 0
    return root.height


def insert(root, key):
    if not root:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getHeight(root.left) - getHeight(root.right)
    if balance > 1:
        if key < root.left.key:
            return rightRotate(root)
        else:
            root.left = leftRotate(root.left)
            return rightRotate(root)
    if balance < -1:
        if key > root.right.key:
            return leftRotate(root)
        else:
            root.right = rightRotate(root.right)
            return leftRotate(root)
    return root


def leftRotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y


def rightRotate(y):
    x = y.left
    T3 = x.right
    x.right = y
    y.left = T3
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x