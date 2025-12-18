"""
QUESTION:
Write a function called `calculate_pizza_options` that takes in a dictionary of pizza options with their respective ingredients, nutritional information, serving size, and price, as well as the number of attendees and a budget. The function should calculate and return the cost and number of pizzas for each pizza option that can satisfy the entire group without exceeding the allocated budget.

Restrictions: The number of attendees should be an integer and the budget should be a float. The dictionary of pizza options should have the following keys: "ingredients", "nutrition", "serving_size", and "price". The "nutrition" key should have the following sub-keys: "calories", "fat", "carbs", and "protein". The function should use the `math.ceil` function to round up the number of pizzas needed to the nearest whole number.
"""

import math

def calculate_pizza_options(pizza_options, attendees, budget):
    """
    Calculate the cost and number of pizzas for each pizza option that can satisfy the entire group without exceeding the allocated budget.

    Args:
        pizza_options (dict): A dictionary of pizza options with their respective ingredients, nutritional information, serving size, and price.
        attendees (int): The number of attendees.
        budget (float): The allocated budget.

    Returns:
        dict: A dictionary with the total cost and number of pizzas for each pizza option.
    """

    result = {}
    for pizza in pizza_options:
        servings_needed = attendees / pizza_options[pizza]["serving_size"]
        pizzas_needed = math.ceil(servings_needed)
        total_cost = pizzas_needed * pizza_options[pizza]["price"]
        if total_cost <= budget:
            result[pizza] = {
                "Total Cost": total_cost,
                "Total Servings": pizzas_needed * pizza_options[pizza]["serving_size"],
                "Number of Pizzas": pizzas_needed
            }
    return result