"""
QUESTION:
Write a function named `handle_non_unique_selection` that takes a list of items and the selected item as input, and returns the correct item even if there are multiple items with the same label, text, or value. The function should uniquely identify each item, such as by its position in the list or by an invisible unique ID.
"""

def handle_non_unique_selection(items, selected_item):
    """
    Returns the correct item even if there are multiple items with the same label, text, or value.

    This function uniquely identifies each item by its position in the list.

    Args:
        items (list): A list of items.
        selected_item: The selected item.

    Returns:
        The correct item from the list.
    """

    # Create a dictionary to store items with their indices as unique identifiers
    item_dict = {index: item for index, item in enumerate(items)}

    # Find the index of the selected item
    for index, item in item_dict.items():
        if item == selected_item:
            return item_dict[index]