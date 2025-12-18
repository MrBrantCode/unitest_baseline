"""
QUESTION:
Create a function `merge_trees` that merges two binary search trees (`root1` and `root2`) into a new balanced binary search tree. The input trees are represented by their root nodes (`root1` and `root2`), and each node has an integer value and references to its left and right children. The function should return the root node of the new balanced binary search tree.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def store_inorder(root, inorder):
    if root is None:
        return
    store_inorder(root.left, inorder)
    inorder.append(root.data)
    store_inorder(root.right, inorder)

def merge(arr1, arr2):
    return sorted(arr1 + arr2)
    
def array_to_bst(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = array_to_bst(arr[:mid])
    root.right = array_to_bst(arr[mid+1:])
    return root

def merge_trees(root1, root2):
    inorder1, inorder2 = [], []
    store_inorder(root1, inorder1)
    store_inorder(root2, inorder2)
    merged_array = merge(inorder1, inorder2)
    return array_to_bst(merged_array)