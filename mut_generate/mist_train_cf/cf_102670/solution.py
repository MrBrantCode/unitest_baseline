"""
QUESTION:
Implement a function `delete_item(lst, item)` that deletes the specified `item` from the list `lst` without using built-in list methods like `remove()` or `pop()`. The function should return the list after deletion and have a time complexity less than O(n), where n is the length of the list.
"""

def delete_item(lst, item):
    return [x for x in lst if x != item]