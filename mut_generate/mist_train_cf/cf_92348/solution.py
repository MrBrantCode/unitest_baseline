"""
QUESTION:
Write a function `delete_4th_element(lst)` that deletes the 4th element from a list `lst`. The list may contain up to 10,000 elements, may have duplicate elements, and must be modified in-place. The function should handle cases where the list has less than 4 elements and optimize for time complexity. Do not use built-in functions or methods that directly delete elements from a list.
"""

def delete_4th_element(lst):
    if len(lst) < 4:
        return lst  

    lst[3] = None  
    lst_len = len(lst)
    new_len = lst_len - 1

    for i in range(4, lst_len):
        lst[i - 1] = lst[i]

    del lst[new_len]

    return lst