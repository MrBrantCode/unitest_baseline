"""
QUESTION:
Create a function `remove_item` that takes a list `lst` and an item `item` as inputs, and returns a new list with all occurrences of `item` removed from `lst`. The function should not use the built-in `remove` function and should have a time complexity of O(n).
"""

def remove_item(lst, item):
    new_lst = []
    for i in lst:
        if i != item:
            new_lst.append(i)
    return new_lst