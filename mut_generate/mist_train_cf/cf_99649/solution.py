"""
QUESTION:
Given a shopping list and filters for organic, gluten-free, vegetarian, and nut-free items, write a function `filter_shopping_list` that takes these as input and returns a list of items that satisfy all the filters. Assume the filters are lists of item names and the shopping list is also a list of item names.
"""

def filter_shopping_list(shopping_list, organic_items, gluten_free_items, vegetarian_items, nut_free_items):
    return list(set(shopping_list) & set(organic_items) & set(gluten_free_items) & set(vegetarian_items) & set(nut_free_items))