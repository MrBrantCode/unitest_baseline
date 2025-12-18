"""
QUESTION:
Write a function `remove_by_index(lst, index)` that takes a list `lst` and an integer `index` as input. The function should remove the element at the specified `index` from the list if the index is valid (i.e., `0 <= index < len(lst)`). If the index is out of range, the function should print an error message. The function should return the updated list.
"""

def remove_by_index(lst, index):
    if index >= 0 and index < len(lst):
        del lst[index]
    else:
        print(f'Index {index} is out of range.')
    return lst