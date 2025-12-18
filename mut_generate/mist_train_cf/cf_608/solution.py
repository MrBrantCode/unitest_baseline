"""
QUESTION:
Write a function called `delete_item` that takes a list `lst` and an item as input and returns a new list with all occurrences of the item removed. The function should not use any built-in list methods like `remove()` or `pop()`. The time complexity of the function should be O(n), where n is the length of the list.
"""

def delete_item(lst, item):
    i = j = 0
    while i < len(lst):
        if lst[i] == item:
            i += 1
        else:
            lst[j] = lst[i]
            i += 1
            j += 1
    return lst[:j]