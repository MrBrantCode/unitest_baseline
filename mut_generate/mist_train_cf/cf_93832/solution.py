"""
QUESTION:
Delete all occurrences of a specified item from a list without using built-in functions or methods like `remove()` or `pop()`. The function should handle duplicate items in the list and maintain a time complexity less than O(n^2). Implement the function `delete_item(lst, item)`, where `lst` is the input list and `item` is the item to be deleted.
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