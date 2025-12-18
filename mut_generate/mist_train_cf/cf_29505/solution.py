"""
QUESTION:
Implement a function `createMenuStructure` that takes a list of menu items as input and returns a hierarchical menu structure represented as a nested dictionary. Each menu item is represented by a string containing the menu item name. The menu items are organized in the order they appear in the list, with "Utility" being the parent of "Reset Password". The function should return a dictionary where the keys are the menu item names and the values are either None for leaf nodes or another dictionary for submenus.
"""

def createMenuStructure(menu_items):
    menu_structure = {}
    current_level = menu_structure

    for item in menu_items:
        if item == "Reset Password":
            current_level[item] = None
        else:
            current_level[item] = {}
            current_level = current_level[item]

    return menu_structure