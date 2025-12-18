"""
QUESTION:
Create a function `delete_element` that takes two parameters: a list `lst` and an integer `index`. The function should remove the element at the specified `index` from `lst` without using any built-in list methods or functions, and return the resulting list. If `index` is out of range, return "Invalid index".
"""

def delete_element(lst, index):
    if index < 0 or index >= len(lst):
        return "Invalid index"
    
    new_lst = []
    for i in range(len(lst)):
        if i != index:
            new_lst.append(lst[i])
    
    return new_lst