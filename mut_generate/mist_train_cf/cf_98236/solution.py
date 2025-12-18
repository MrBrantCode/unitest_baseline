"""
QUESTION:
Create a function `categorize_ingredients` that takes in two parameters: a list of ingredient names and a list of category names. The function should return a dictionary where the keys are the category names and the values are dictionaries with the ingredient names as keys and a quantity as values. Each ingredient can belong to multiple categories.
"""

def categorize_ingredients(ingredients, categories):
    categorized = {}
    for ingredient in ingredients:
        for category in categories:
            if ingredient in category:
                if category not in categorized:
                    categorized[category] = {}
                categorized[category][ingredient] = 1  # quantity can be set to any value
    return categorized