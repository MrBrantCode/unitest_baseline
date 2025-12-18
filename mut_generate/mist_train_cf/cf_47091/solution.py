"""
QUESTION:
Create a function named `equal_trees` that checks if two Binary Search Trees (BSTs) are equal. The function should consider both the node values and the structure of the trees. It should handle edge cases such as empty trees or trees with duplicate values. The input BSTs are initially represented as lists and need to be converted into a binary tree structure before comparison.
"""

class Node: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key

def insert_level_order(arr, root, i, n):   
    if i < n: 
        temp = Node(arr[i])  
        root = temp  
  
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)  
  
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n) 
    return root 

def equal_trees(t1, t2): 
    if t1 is None and t2 is None: 
        return True
    elif t1 is None or t2 is None:
        return False
    else: 
        return ((t1.val == t2.val) and
                equal_trees(t1.left , t2.left) and
                equal_trees(t1.right, t2.right))