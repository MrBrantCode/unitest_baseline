"""
QUESTION:
Create a function called `filter_shopping_list` that takes in a shopping list and returns a new list containing only the items that are organic, gluten-free, vegetarian, and nut-free.
"""

def filter_shopping_list(shopping_list, organic_items, gluten_free_items, vegetarian_items, nut_free_items):
    """
    Filter a shopping list based on organic, gluten-free, vegetarian, and nut-free criteria.

    Args:
    shopping_list (list): The shopping list to filter.
    organic_items (list): The list of organic items.
    gluten_free_items (list): The list of gluten-free items.
    vegetarian_items (list): The list of vegetarian items.
    nut_free_items (list): The list of nut-free items.

    Returns:
    list: The filtered shopping list.
    """
    return list(set(shopping_list) & set(organic_items) & set(gluten_free_items) & set(vegetarian_items) & set(nut_free_items))