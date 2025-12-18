"""
QUESTION:
Create a function called `count_inventory` that takes a dictionary `inventory` with two keys, "fruits" and "vegetables", each containing a list of items. The function should return a dictionary with the same keys, but the values should be dictionaries where each key is a unique item and the value is the count of that item.
"""

def count_inventory(inventory):
    """
    This function takes a dictionary of inventory with 'fruits' and 'vegetables' as keys and returns 
    a dictionary where each key is a unique item and the value is the count of that item.

    Args:
        inventory (dict): A dictionary with 'fruits' and 'vegetables' as keys and list of items as values.

    Returns:
        dict: A dictionary with 'fruits' and 'vegetables' as keys and dictionaries of item counts as values.
    """

    count = {
        "fruits": {},
        "vegetables": {}
    }

    # Iterate over each fruit and count their occurrence 
    for fruit in inventory["fruits"]:
        if fruit in count["fruits"]:
            count["fruits"][fruit] += 1
        else:
            count["fruits"][fruit] = 1

    # Iterate over each vegetable and count their occurrence
    for vegetable in inventory["vegetables"]:
        if vegetable in count["vegetables"]:
            count["vegetables"][vegetable] += 1
        else:
            count["vegetables"][vegetable] = 1

    return count