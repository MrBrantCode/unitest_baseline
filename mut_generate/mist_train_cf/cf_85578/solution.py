"""
QUESTION:
Create a program with three functions: `search_item`, `add_item`, and `remove_item`. The `search_item` function takes a list `list_items` and an `item_to_search` as input and returns the positions of `item_to_search` in `list_items`. If `item_to_search` is not found, it returns a message indicating so. The `add_item` function takes a list `list_items` and an `item_to_add` as input, adds `item_to_add` to `list_items`, and returns the sorted list. The `remove_item` function takes a list `list_items` and an `item_to_remove` as input, removes all occurrences of `item_to_remove` from `list_items`, and returns the sorted list.
"""

def search_item(list_items, item_to_search):
    positions = []
    for i in range(len(list_items)):
        if list_items[i] == item_to_search:
            positions.append(i)
    
    if positions:
        return f'Item "{item_to_search}" found at positions {positions}'
    else:
        return f'Item "{item_to_search}" not found in the list.'

def add_item(list_items, item_to_add):
    list_items.append(item_to_add)
    list_items.sort()
    return list_items

def remove_item(list_items, item_to_remove):
    while item_to_remove in list_items:
        list_items.remove(item_to_remove)
    return list_items