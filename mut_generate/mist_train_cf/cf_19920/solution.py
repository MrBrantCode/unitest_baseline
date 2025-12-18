"""
QUESTION:
Create a function called `modify_tuples_list` that takes a list of tuples as input, removes any tuples that have duplicate elements, sorts the modified list in descending order based on the length of the tuples, and returns the modified list.
"""

def modify_tuples_list(lst):
    modified_lst = []

    for tup in lst:
        if len(set(tup)) == len(tup):
            modified_lst.append(tup)

    modified_lst.sort(key=len, reverse=True)
    return modified_lst