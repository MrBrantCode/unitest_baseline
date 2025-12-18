"""
QUESTION:
Implement a function `countLarger` that takes a list of numbers as input and returns a list where each element at index `i` is the count of elements in the input list that are larger than the element at index `i`. The function should use a binary search tree (BST) data structure to achieve this. The BST node should have a `val`, `left`, `right`, and `count` attribute where `val` is the node value, `left` and `right` are the left and right child nodes, and `count` is the count of nodes in the subtree rooted at this node. The function should return a list of counts in the same order as the input list.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.count = 1

def insert(node, insert_val):
    if node is None:
        return TreeNode(insert_val)
    elif insert_val <= node.val:
        node.count += 1
        return TreeNode(node.val, insert(node.left, insert_val), node.right)
    else:  
        return TreeNode(node.val, node.left, insert(node.right, insert_val))

def countLarger(nums):
    tree = None
    result = []
    for num in reversed(nums):
        count_larger = 0
        current = tree
        while current is not None:
            if current.val < num:
                count_larger += current.count
                current = current.right
            else:
                current = current.left
        tree = insert(tree, num)
        result.append(count_larger)
    return list(reversed(result))