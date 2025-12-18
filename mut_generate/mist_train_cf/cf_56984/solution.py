"""
QUESTION:
Create a function `merge` that merges two binary search trees into a balanced binary search tree. The function should take as input two lists representing the in-order traversal of the two binary search trees. The new tree should contain no duplicates and each node's value is an integer from 1 to N where N is the total number of unique nodes. The function should return the root of the merged balanced binary search tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def merge(elems1, elems2):
    s = set(elems1 + elems2)  # Merge and remove duplicates
    sorted_elems = sorted(list(s))  # Sort the elements
    return balance(sorted_elems)

def balance(elems):
    if not elems:
        return None

    mid = len(elems) // 2  # Find the middle element
    root = Node(elems[mid])  # Create root node
    root.left = balance(elems[:mid])  # Create left subtree
    root.right = balance(elems[mid + 1:])  # Create right subtree
    return root