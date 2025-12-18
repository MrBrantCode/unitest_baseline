"""
QUESTION:
Implement a function `search_recipes` that takes in a list of ingredients and dietary restrictions as input and returns a list of recipes that match the given criteria. The function should have a time complexity of O(n), where n is the number of recipes in the database. Assume that the recipes are stored in a list of dictionaries, where each dictionary represents a recipe and contains the keys 'ingredients' and 'dietary_restrictions'.
"""

def search_recipes(recipes, ingredients, dietary_restrictions):
    """
    Searches for recipes that match the given ingredients and dietary restrictions.

    Args:
        recipes (list): A list of dictionaries representing recipes.
        ingredients (list): A list of ingredients to search for.
        dietary_restrictions (list): A list of dietary restrictions to consider.

    Returns:
        list: A list of recipes that match the given criteria.
    """
    # Initialize an empty list to store the matching recipes
    matching_recipes = []

    # Iterate over each recipe in the database
    for recipe in recipes:
        # Check if all ingredients are present in the recipe
        if all(ingredient in recipe['ingredients'] for ingredient in ingredients):
            # Check if the recipe meets all dietary restrictions
            if all(restriction in recipe['dietary_restrictions'] for restriction in dietary_restrictions):
                # If both conditions are met, add the recipe to the list of matching recipes
                matching_recipes.append(recipe)

    # Return the list of matching recipes
    return matching_recipes