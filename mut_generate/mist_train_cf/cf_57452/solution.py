"""
QUESTION:
Implement a function `insert(value, root)` that inserts a value into a skew heap and returns the root of the resulting heap. The function should use the `merge_roots(node1, node2)` helper function, which merges two skew heap roots into a single heap and returns the root of the resulting heap. The `merge_roots(node1, node2)` function should maintain the skew heap property by ensuring the smaller value is at the root and swapping the left and right subtrees of the root after merging.
"""

class HeapNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def merge_roots(node1, node2):
    if node1 is None:
        return node2
    if node2 is None:
        return node1

    # Swap values if node2 value is smaller
    if node2.value < node1.value:
        temp = node2
        node2 = node1
        node1 = temp

    # Node2 is merged with right subtree of node1 and then both children of node1 are swapped
    node1.right = merge_roots(node1.right, node2)
    node1.left, node1.right = node1.right, node1.left

    return node1


def entrance(value, root):
    node = HeapNode(value)
    return merge_roots(root, node)