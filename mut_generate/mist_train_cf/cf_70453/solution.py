"""
QUESTION:
Create a function named `deepcopy` that takes a multi-dimensional list of integers as input and returns a deep copy of the list. The function should not use the built-in `copy` module or any other function that directly clones objects. It should be able to handle lists of any feasible length and depth.
"""

def deepcopy(lst):
    new_lst = []
    for item in lst:
        if type(item) == list:
            new_lst.append(deepcopy(item))
        else:
            new_lst.append(item)
    return new_lst