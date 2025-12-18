"""
QUESTION:
Filter the given shopping list to include only organic, gluten-free, vegetarian, and nut-free items. The function name should be `filter_shopping_list`. The function takes four lists as input parameters: `shopping_list`, `organic_items`, `gluten_free_items`, `vegetarian_items`, and `nut_free_items`. The function should return the filtered list of items.
"""

def filter_shopping_list(shopping_list, organic_items, gluten_free_items, vegetarian_items, nut_free_items):
    """
    This function filters the given shopping list to include only organic, gluten-free, vegetarian, and nut-free items.

    Parameters:
    shopping_list (list): The list of items to be filtered.
    organic_items (list): The list of organic items.
    gluten_free_items (list): The list of gluten-free items.
    vegetarian_items (list): The list of vegetarian items.
    nut_free_items (list): The list of nut-free items.

    Returns:
    list: The filtered list of items.
    """
    return list(set(shopping_list) & set(organic_items) & set(gluten_free_items) & set(vegetarian_items) & set(nut_free_items))