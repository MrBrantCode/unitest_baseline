"""
QUESTION:
Implement the function `find_index(my_list, element, index=0)` to find the index of the first occurrence of the given `element` in a nested list `my_list`. The function should recursively search through the list and its sublists, and return the index of the first occurrence of the `element`. If the `element` is not found, the function should return -1. The solution should have a time complexity of O(n), where n is the length of the list.
"""

def find_index(my_list, element, index=0):
    if my_list == element:
        return index
    
    for i in range(len(my_list)):
        if isinstance(my_list[i], list):
            sub_index = find_index(my_list[i], element, index + i)
            if sub_index != -1:
                return sub_index
        elif my_list[i] == element:
            return index + i
    
    return -1