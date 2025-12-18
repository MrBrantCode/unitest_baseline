"""
QUESTION:
Write a function named `filter_shopping_list` that takes four lists of items as input: `shopping_list`, `organic_items`, `gluten_free_items`, `vegetarian_items`, and `nut_free_items`. This function should return a list of items that are present in all of the input lists, representing the items that meet all the specified criteria. The function should work with any input lists, not just the ones provided in the example.
"""

def filter_shopping_list(shopping_list, organic_items, gluten_free_items, vegetarian_items, nut_free_items):
    return list(set(shopping_list) & set(organic_items) & set(gluten_free_items) & set(vegetarian_items) & set(nut_free_items))