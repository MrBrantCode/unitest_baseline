"""
QUESTION:
Create a function named `add_item` that adds a new item at a specific index in a given list. The function should take three parameters: the list, the index where the item will be added, and the item to be added. It should also handle cases where the provided index is out of the list's range, returning an error message in such cases. The function should modify the original list.
"""

def add_item(item_list, index, item):
    try:
        item_list.insert(index, item)
    except IndexError:
        print("Index is out of the range of the list!")
        return None
    return item_list