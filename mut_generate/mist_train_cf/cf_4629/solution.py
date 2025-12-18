"""
QUESTION:
Create a function `is_proper_subset(set1, set2)` that returns True if `set1` is a proper subset of `set2`, meaning every element in `set1` is present in `set2` but `set2` has at least one additional element. Both sets must be of the same data type, otherwise, an exception is raised. If both sets are empty, the function returns False. If one set is empty and the other set is not, the function returns True if the non-empty set is a proper subset of the empty set and False otherwise.
"""

def is_proper_subset(set1, set2):
    if type(set1) != type(set2):
        raise Exception("Sets must be of the same data type")
    
    if len(set1) == 0 and len(set2) == 0:
        return False
    
    if len(set1) == 0:
        return True
    
    if len(set2) == 0:
        return False
    
    return set1.issubset(set2) and len(set1) < len(set2)