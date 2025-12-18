"""
QUESTION:
Write a function called `remove_dup` that takes a list as input, which can contain various data types including nested lists and dictionaries. The function should remove duplicates from the list, considering nested lists and dictionaries with the same elements but different orders as duplicates. The function should be robust enough to handle errors and edge cases, and it should not use a set to remove duplicates because lists and dictionaries are unhashable types.
"""

def remove_dup(lst):
    no_dup_lst = []  
    for i in lst: 
        if isinstance(i, list):
            i = tuple(sorted(i))  # convert list to tuple and sort it
        elif isinstance(i, dict):
            i = tuple(sorted(i.items()))  # convert dict to tuple and sort it
        if i not in no_dup_lst: 
            no_dup_lst.append(i) 
    return no_dup_lst