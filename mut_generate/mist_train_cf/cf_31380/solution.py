"""
QUESTION:
Create a function called `manage_inventory` that takes in an inventory dictionary and two parameters, an item ID and an action. The function should perform the action on the specified item ID in the inventory. 

- The inventory is represented as a dictionary where keys are item IDs (integers) and values are the quantity of each item (integers).
- The action can be either "add" to add the item to the inventory or "consume" to consume the item from the inventory.
- If the action is "add", add the item ID to the inventory and set its quantity to 1 if it doesn't already exist, or increment the quantity by 1 if it does exist.
- If the action is "consume", decrement the quantity of the item ID by 1 if it exists in the inventory. If the quantity becomes 0, the item should be removed from the inventory.
- The function should return the updated inventory after performing the specified action.
"""

def manage_inventory(inventory, item_id, action):
    if action == "add":
        if item_id in inventory:
            inventory[item_id] += 1
        else:
            inventory[item_id] = 1
    elif action == "consume":
        if item_id in inventory:
            inventory[item_id] -= 1
            if inventory[item_id] == 0:
                del inventory[item_id]
    return inventory