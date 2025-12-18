"""
QUESTION:
Create a function `is_subset(set1, set2)` that checks if all elements of `set1` are present in `set2`, where both sets can contain nested lists and no duplicates are allowed. The function should return `True` if `set1` is a subset of `set2`, and `False` otherwise. The comparison should also work for nested lists within the sets.
"""

def entrance(set1, set2):
    list1 = list(set1)
    list2 = list(set2)
    
    for i in list1:
        if i not in list2:
            return False
    
    return True