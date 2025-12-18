"""
QUESTION:
Implement a function `remove_element_and_neighbors` that takes two parameters: a list `lst` and a number `num`. The function should remove all occurrences of `num` in `lst` along with its neighboring elements (both before and after) and return the modified list. If `num` is at the start or end of the list, remove only the element and its one neighbor.
"""

def remove_element_and_neighbors(lst, num):
    i = 0
    while i < len(lst):
        if lst[i] == num:
            if i == 0: # if it's the first element
                del lst[i:i+2]
            elif i == len(lst) - 1: # if it's the last element
                del lst[i-1:i+1]
            else: 
                del lst[i-1:i+2]
        else: 
            i += 1
    return lst