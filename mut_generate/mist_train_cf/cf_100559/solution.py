"""
QUESTION:
Create a function called `categorize_ingredients` that takes in a list of ingredient names and a list of categories as input, and returns a dictionary where the keys are the categories and the values are dictionaries with ingredient names as keys and quantities as values. The function should handle cases where an ingredient belongs to multiple categories. Assume that an ingredient belongs to a category if the ingredient name is a substring of the category name.
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