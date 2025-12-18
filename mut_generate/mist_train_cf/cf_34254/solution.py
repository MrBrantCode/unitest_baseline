"""
QUESTION:
Implement a class `InventoryManager` with methods `add_item(item_name)`, `remove_item(item_name)`, and `display_inventory()`. The class should manage a set of unique items where the same item name with different capitalization is treated as the same item. The `add_item(item_name)` method should add an item to the inventory, the `remove_item(item_name)` method should remove an item from the inventory, and the `display_inventory()` method should print the current inventory list in alphabetical order.
"""

def entrance(item_name, action, inventory=None):
    if inventory is None:
        inventory = set()
    
    item_name = item_name.lower()
    
    if action == 'add':
        inventory.add(item_name)
    elif action == 'remove':
        if item_name in inventory:
            inventory.remove(item_name)
    elif action == 'display':
        sorted_inventory = sorted(inventory)
        return sorted_inventory

    return inventory