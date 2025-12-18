"""
QUESTION:
Create a function `search_recipes` that filters recipes based on dietary restrictions, calorie count, cooking time, and type of cuisine. The function should take in the following parameters: `dietary_restrictions`, `calories`, `cooking_time`, and `cuisine`. It should return a list of recipes that match the given criteria. Assume that a recipe is represented by a dictionary with the keys `name`, `ingredients`, `dietary_restrictions`, `calories`, `cooking_time`, and `cuisine`. The function should be able to handle a list of recipes as input and return a filtered list of recipes.
"""

def search_recipes(recipes, dietary_restrictions, calories, cooking_time, cuisine):
    """
    Filters recipes based on dietary restrictions, calorie count, cooking time, and type of cuisine.

    Args:
        recipes (list): A list of recipes. Each recipe is a dictionary with keys 'name', 'ingredients', 
                        'dietary_restrictions', 'calories', 'cooking_time', and 'cuisine'.
        dietary_restrictions (str): The dietary restrictions to filter by.
        calories (int): The maximum calorie count to filter by.
        cooking_time (str): The maximum cooking time to filter by.
        cuisine (str): The type of cuisine to filter by.

    Returns:
        list: A list of recipes that match the given criteria.
    """

    filtered_recipes = []
    for recipe in recipes:
        if (dietary_restrictions in recipe['dietary_restrictions'] and
            recipe['calories'] <= calories and
            recipe['cooking_time'] <= cooking_time and
            recipe['cuisine'] == cuisine):
            filtered_recipes.append(recipe)

    return filtered_recipes