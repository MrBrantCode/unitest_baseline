"""
QUESTION:
Create a function named `manage_inventory` that takes a nested dictionary `inventory` where the outer keys are categories and the inner keys are item names with their corresponding country of origin as values. The function should sort the dictionary in descending order by the number of items in each category and return the sorted dictionary. Additionally, the function should allow the removal of items from the dictionary based on their name and country of origin, and return the updated dictionary.
"""

def manage_inventory(inventory, remove_item=None, remove_country=None):
    # Sort the dictionary in descending order by the number of items in each category
    sorted_inventory = dict(sorted(inventory.items(), key=lambda x: len(x[1]), reverse=True))

    # Remove items from the dictionary based on their name and country of origin
    if remove_item and remove_country:
        for category, items in sorted_inventory.items():
            if remove_item in items and items[remove_item] == remove_country:
                items.pop(remove_item)

    return sorted_inventory