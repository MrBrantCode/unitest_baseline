"""
QUESTION:
Write a function called `modify_tuples_list` that takes a list of tuples as input, removes any tuples that have a duplicate element, and sorts the modified list in descending order based on the length of the tuples.
"""

def modify_tuples_list(lst):
    modified_lst = [tup for tup in lst if len(set(tup)) == len(tup)]
    modified_lst.sort(key=len, reverse=True)
    return modified_lst