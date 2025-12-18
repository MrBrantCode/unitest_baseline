"""
QUESTION:
Write a function `count_item_and_sublists(lst, item)` that takes a list `lst` and an item as input, and returns a tuple containing the total count of the item in the list and the count of sublists that contain the item. The function should support nested list structures.
"""

def count_item_and_sublists(lst, item):
    item_count = 0
    sublist_count = 0

    for i in lst:
        if isinstance(i, list):
            sublist_item_count, sublist_sublist_count = count_item_and_sublists(i, item)
            item_count += sublist_item_count
            if sublist_item_count > 0:  # item is present in the sublist
                sublist_count += 1
        elif i == item:
            item_count += 1

    return item_count, sublist_count