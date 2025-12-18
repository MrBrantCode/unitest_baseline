"""
QUESTION:
Implement a function `convertToMenuHierarchy` that takes a list of menu items as input, where each item is a string containing the name of the menu item, and returns a nested dictionary representing the menu hierarchy. The input list may contain sub-items denoted by " > " (e.g., "Products > Laptops"). Each key in the output dictionary should represent a menu item, with its corresponding value being another dictionary representing its sub-items. If a menu item has no sub-items, its value should be an empty dictionary.
"""

def convertToMenuHierarchy(menu_items):
    menu_hierarchy = {}

    for item in menu_items:
        parts = item.split(" > ")
        current_level = menu_hierarchy

        for part in parts:
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]

    return menu_hierarchy