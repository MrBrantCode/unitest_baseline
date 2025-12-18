"""
QUESTION:
Create a function called `calculate_pizza_ingredients` that determines the quantity of ingredients needed to make a specified number of vegetarian pizzas with gluten-free bases. The function should take the number of pizzas as input and return the quantities of tomatoes, bell peppers, cheese, and gluten-free flour required. Assume each pizza requires 4 tomatoes, 2 bell peppers, and 1 kg of cheese, and a 500g bag of gluten-free flour makes 2 pizza bases.
"""

def calculate_pizza_ingredients(num_pizzas):
    """
    Calculate the quantity of ingredients needed for a specified number of vegetarian pizzas.

    Args:
        num_pizzas (int): The number of pizzas to make.

    Returns:
        dict: A dictionary containing the quantities of tomatoes, bell peppers, cheese, and gluten-free flour required.
    """
    tomatoes = num_pizzas * 4
    bell_peppers = num_pizzas * 2
    cheese = num_pizzas * 1  # in kg
    gluten_free_flour = (num_pizzas * 250) / 1000  # convert grams to kg

    return {
        "tomatoes": tomatoes,
        "bell_peppers": bell_peppers,
        "cheese": cheese,
        "gluten_free_flour": gluten_free_flour
    }