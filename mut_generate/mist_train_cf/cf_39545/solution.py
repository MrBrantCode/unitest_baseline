"""
QUESTION:
Write a function `parse_items` that takes a list of strings as input, where each item name is followed by its price as a string representing a floating-point number. Return a dictionary where the keys are the item names and the values are the corresponding prices. Assume the input list always follows the pattern of an item name on one line followed by its price on the next line.
"""

def parse_items(items_list):
    items_dict = {}
    for i in range(0, len(items_list), 2):
        item_name = items_list[i]
        item_price = float(items_list[i + 1])
        items_dict[item_name] = item_price
    return items_dict