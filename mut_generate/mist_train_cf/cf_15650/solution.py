"""
QUESTION:
Create a function `delete_item(lst, item)` that deletes all occurrences of `item` from the list `lst` without using built-in functions or methods like `remove()` or `pop()`. The function should have a time complexity less than O(n), where n is the length of the list, and handle lists with duplicate items and millions of elements.
"""

def delete_item(lst, item):
    left = 0
    right = 0

    while right < len(lst):
        if lst[right] != item:
            lst[left] = lst[right]
            left += 1
        right += 1

    del lst[left:]

    return lst