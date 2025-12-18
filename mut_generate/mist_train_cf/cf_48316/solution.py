"""
QUESTION:
Given a list of dictionaries, create a new list that excludes any dictionaries that are a subset of another dictionary in the list. Write a function called `remove_subsets` that takes a list of dictionaries as input and returns the new list of dictionaries. The function should have a reasonable time complexity for small to medium-sized input lists.
"""

def entrance(lst):
    n = len(lst)
    res = []
    for i in range(n):
        is_subset = any(all(item in lst[j].items() for item in lst[i].items()) 
                        for j in range(n) if j != i)
        if not is_subset:
            res.append(lst[i])
    return res