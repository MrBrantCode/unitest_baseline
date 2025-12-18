"""
QUESTION:
Write a function named `generate_shopping_list` that takes in three parameters: `guests` (a dictionary mapping guest names to their dietary restrictions), `food_items` (a dictionary mapping food items to their ingredients), and `required_quantities` and `item_costs` (dictionaries mapping food items to their required quantities and estimated costs, respectively). The function should return a dictionary representing the shopping list with the required quantities of each item and the estimated total cost. Note that the function should consider the dietary restrictions of each guest and only include items that do not conflict with their restrictions.
"""

def generate_shopping_list(guests, food_items, required_quantities, item_costs):
    """
    Generate a shopping list considering the dietary restrictions of each guest.

    Args:
    guests (dict): A dictionary mapping guest names to their dietary restrictions.
    food_items (dict): A dictionary mapping food items to their ingredients.
    required_quantities (dict): A dictionary mapping food items to their required quantities.
    item_costs (dict): A dictionary mapping food items to their estimated costs.

    Returns:
    dict: A dictionary representing the shopping list with the required quantities of each item and the estimated total cost.
    """
    shopping_list = {}
    for guest, restrictions in guests.items():
        for item, ingredients in food_items.items():
            if all(ingredient not in restrictions for ingredient in ingredients):
                if item in shopping_list:
                    shopping_list[item] += required_quantities[item]
                else:
                    shopping_list[item] = required_quantities[item]
    total_cost = sum(quantity * item_costs[item] for item, quantity in shopping_list.items())
    shopping_list["total_cost"] = total_cost
    return shopping_list