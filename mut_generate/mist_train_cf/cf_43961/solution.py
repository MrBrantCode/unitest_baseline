"""
QUESTION:
Write a function called `set_intersection` that takes two sets `s1` and `s2` as input and returns their intersection as a list in ascending order, without using any built-in set functions. Instead, implement a binary search tree to find common elements, and ensure that the returned list is de-duplicated.
"""

def set_intersection(s1, s2):
    class BSTNode:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    class BinarySearchTree:
        def __init__(self):
            self.root = None
        
        def insert(self, value):
            if self.root is None:
                self.root = BSTNode(value)
            else:
                self.insert_node(self.root, value)
        
        def insert_node(self, current_node, value):
            if value < current_node.value:
                if current_node.left:
                    self.insert_node(current_node.left, value)
                else:
                    current_node.left = BSTNode(value)
            elif value > current_node.value:
                if current_node.right:
                    self.insert_node(current_node.right, value)
                else:
                    current_node.right = BSTNode(value)
        
        def in_bst(self, current_node, value):
            if current_node is None:
                return False
            if current_node.value == value:
                return True
            elif current_node.value > value:
                return self.in_bst(current_node.left, value)
            else:
                return self.in_bst(current_node.right, value)

    bst = BinarySearchTree()
    for elem in s1:
        bst.insert(elem)

    intersection = []
    for elem in s2:
        if bst.in_bst(bst.root, elem) and elem not in intersection:
            intersection.append(elem)

    intersection.sort()
    return intersection