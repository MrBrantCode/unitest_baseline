"""
QUESTION:
Implement a function `search_bst(root, key)` that takes in the root of a binary search tree (BST) and a key to search for. The function should return the number of comparisons made during the search. If the key does not exist in the BST, return -1.

Constraints:
- The BST can have up to 10^6 nodes.
- The keys in the BST are unique.
- The function should have a time complexity of O(log n) in the average case, where n is the number of nodes in the BST.
- The function should have a space complexity of O(1).
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_bst(root, key):
    comparisons = 0
    current = root

    while current is not None:
        comparisons += 1

        if current.value == key:
            return comparisons
        elif current.value < key:
            current = current.right
        else:
            current = current.left

    return -1