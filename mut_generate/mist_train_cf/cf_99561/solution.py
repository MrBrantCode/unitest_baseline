"""
QUESTION:
Write a function `recommend_dish` that takes two parameters: `available_dishes` and `ingredients`. `available_dishes` is a dictionary where the key is the name of the dish and the value is another dictionary containing the required ingredients with their respective quantities. `ingredients` is a dictionary containing the available ingredients with their respective quantities. The function should return the name of the dish that can be made with the given ingredients and the quantity of remaining ingredients, if any. If no dish can be made, return a message indicating that.
"""

def recommend_dish(available_dishes, ingredients):
    """
    Recommend a dish based on the given ingredients.
    
    Parameters:
    available_dishes (dict): A dictionary where the key is the name of the dish and the value is another dictionary containing the required ingredients with their respective quantities.
    ingredients (dict): A dictionary containing the available ingredients with their respective quantities.
    
    Returns:
    tuple: A tuple containing the name of the recommended dish and the quantity of remaining ingredients. If no dish can be made, return a message indicating that.
    """
    # Find dishes that can be made with the given ingredients
    possible_dishes = []
    for dish, required_ingredients in available_dishes.items():
        if all(ingredient in ingredients.keys() and ingredients[ingredient] >= required_ingredients[ingredient] for ingredient in required_ingredients.keys()):
            possible_dishes.append(dish)
    # Return the recommended dish and the quantity of remaining ingredients
    if len(possible_dishes) > 0:
        recommended_dish = possible_dishes[0]
        remaining_ingredients = {ingredient: ingredients[ingredient] - available_dishes[recommended_dish][ingredient] for ingredient in available_dishes[recommended_dish].keys()}
        return (recommended_dish, remaining_ingredients)
    else:
        return "No dish can be made with the given ingredients."