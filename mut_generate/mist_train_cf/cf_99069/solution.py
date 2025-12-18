"""
QUESTION:
Write a function called `filter_shopping_list` that takes in two parameters: `shopping_list` and a dictionary `filters`. The `filters` dictionary contains four keys: `organic`, `gluten_free`, `vegetarian`, and `nut_free`, each mapping to a list of items that meet the corresponding criteria. The function should return a list of items from `shopping_list` that meet all the filter criteria.
"""

def filter_shopping_list(shopping_list, filters):
    """
    Filter the shopping list based on the provided filters.

    Args:
        shopping_list (list): The list of items to filter.
        filters (dict): A dictionary containing the filter criteria.
            The dictionary should have the following keys:
            - organic
            - gluten_free
            - vegetarian
            - nut_free

            Each key should map to a list of items that meet the corresponding criteria.

    Returns:
        list: The filtered list of items.
    """
    filtered_list = set(shopping_list)
    for filter_name, filter_items in filters.items():
        filtered_list &= set(filter_items)
    return list(filtered_list)