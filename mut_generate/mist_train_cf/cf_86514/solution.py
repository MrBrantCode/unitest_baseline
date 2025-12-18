"""
QUESTION:
Write a function `delete_item` that takes a list `lst` and an item as input and returns a new list with all occurrences of the item removed. The function should have a time complexity less than O(n), where n is the length of the list, and should not use any built-in functions or methods like `remove()` or `pop()`. The function should also be able to handle duplicate items and large lists with millions of elements.
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