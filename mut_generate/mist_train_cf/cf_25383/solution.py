"""
QUESTION:
Write a function `are_identical(Tree1, Tree2)` that checks if two binary search trees `Tree1` and `Tree2` are identical. The function should return `True` if the trees are identical and `False` otherwise. The trees are considered identical if they have the same structure and the same node values.
"""

def are_identical(Tree1, Tree2):
    # Both trees are empty 
    if Tree1==None and Tree2==None: 
        return True
  
    # If only one of them is empty 
    if (Tree1==None or Tree2==None): 
        return False
  
    # Both non-empty, compare the data and 
    # recur for left and right sub-tree 
    if (Tree1.data==Tree2.data and 
        are_identical(Tree1.left, Tree2.left)and
        are_identical(Tree1.right, Tree2.right)): 
        return True 
    else: 
        return False