"""
QUESTION:
Write a function called `calculate_pizza_ingredients` to calculate the total quantity of each ingredient needed for a given number of vegetarian pizzas. The function should take two parameters: the number of pizzas and a dictionary of ingredients with their respective quantities per pizza. The function should return a dictionary with the total quantity of each ingredient needed. Assume the ingredients are 'tomatoes', 'bell peppers', and 'cheese'.
"""

def calculate_pizza_ingredients(num_pizzas, ingredients):
    """
    Calculate the total quantity of each ingredient needed for a given number of pizzas.

    Args:
        num_pizzas (int): The number of pizzas to make.
        ingredients (dict): A dictionary of ingredients with their respective quantities per pizza.

    Returns:
        dict: A dictionary with the total quantity of each ingredient needed.
    """
    total_ingredients = {}
    for ingredient, quantity in ingredients.items():
        total_ingredients[ingredient] = quantity * num_pizzas
    return total_ingredients