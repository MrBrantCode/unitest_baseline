"""
QUESTION:
Create a function called `dict_to_bst` that takes a dictionary as input and returns a binary search tree (BST) where each key-value pair in the dictionary is a node in the BST. The BST should be constructed iteratively, without using recursive methodology, and should enable efficient search operations. The BST should have the property that for each node, all elements in the left subtree are less than the node and all elements in the right subtree are greater than the node.
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        if not self.root:
            self.root = Node(key, val)
        else:
            cur = self.root
            while cur:
                if key < cur.key:
                    if cur.left is None:
                        cur.left = Node(key, val)
                        return
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = Node(key, val)
                        return
                    else:
                        cur = cur.right
                        
def dict_to_bst(dictionary):
    bst = BST()
    for key, val in dictionary.items():
        bst.insert(key, val)
    return bst