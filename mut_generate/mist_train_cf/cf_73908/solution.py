"""
QUESTION:
Create a function `remove_duplicates` that takes a list as input and returns a new list with all duplicate elements removed, while maintaining the original order of elements. Do not use any built-in functions for removing duplicates or sorting. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def remove_duplicates(lst):
    new_lst = []
    seen = set()
    for item in lst:
        if item not in seen:  
            new_lst.append(item)
            seen.add(item)
    return new_lst