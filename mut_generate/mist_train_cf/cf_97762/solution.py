"""
QUESTION:
Write a function `eliminate_duplicates` that takes two input lists `list1` and `list2`, eliminates any duplicate entries from the combined list, and returns the resulting list without altering the original input lists. The function must use either the `filter()` or `reduce()` method.
"""

from functools import reduce

def eliminate_duplicates(list1, list2):
    # make a copy of input lists
    list1_copy = list1.copy()
    list2_copy = list2.copy()
    
    # concatenate the two input lists
    combined_list = list1_copy + list2_copy
    
    # use reduce() method to convert list to set and eliminate duplicates
    no_duplicates_set = reduce(lambda x, y: x.union(y), [set(combined_list)])
    
    # convert set back to list and return final output
    no_duplicates_list = list(no_duplicates_set)
    return no_duplicates_list