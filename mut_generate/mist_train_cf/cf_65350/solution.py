"""
QUESTION:
Create a function `find_indices` that takes two lists `first_list` and `second_list` as input and returns the indices of elements in `second_list` as they appear in `first_list`. Implement a binary search tree (BST) to optimize the search operation, ensuring a time complexity of O(log(n)) in the average case. The function should construct the BST from `first_list` and then traverse `second_list` to find the indices of its elements in `first_list`.
"""

class Node:
    def __init__(self, key, index):
        self.left = None
        self.right = None
        self.val = key
        self.index = index

def insert(root, key, index):
    if root is None:
        return Node(key, index)
    else:
        if root.val < key:
            root.right = insert(root.right, key, index)
        else:
            root.left = insert(root.left, key, index)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root.index if root else None
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def find_indices(first_list, second_list):
    n = len(first_list)
    root = None
    for i in range(n):
        root = insert(root, first_list[i], i)
    return [search(root, key) for key in second_list]