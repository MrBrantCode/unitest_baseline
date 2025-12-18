"""
QUESTION:
Create a function called `remove_item` that takes a list `lst` and an item `item` as inputs. Implement a solution that removes all occurrences of `item` from `lst` without using the built-in `remove` function and achieves a time complexity of O(n). The function should return the modified list.
"""

def remove_item(lst, item):
    new_lst = []
    for i in lst:
        if i != item:
            new_lst.append(i)
    return new_lst