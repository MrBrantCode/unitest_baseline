"""
QUESTION:
Fill the blender cup within budget. Create a function called `fill_blender_cup` that takes the initial amounts and prices of two types of juice, the capacity of the blender cup, and the total budget as input. The function should return the amounts of each juice that can be added to fill the cup while staying within the given budget.
"""

def fill_blender_cup(initial_orange, initial_mango, orange_price, mango_price, capacity, budget):
    """
    Calculate the amounts of orange and mango juice to add to fill the blender cup within the given budget.

    Args:
    initial_orange (float): Initial amount of orange juice in the blender cup.
    initial_mango (float): Initial amount of mango juice in the blender cup.
    orange_price (float): Price of orange juice per liter.
    mango_price (float): Price of mango juice per liter.
    capacity (float): Capacity of the blender cup.
    budget (float): Total budget.

    Returns:
    tuple: Amounts of orange and mango juice to add.
    """

    # Calculate the remaining capacity of the blender cup
    remaining_capacity = capacity - initial_orange - initial_mango
    
    # Calculate the remaining budget
    remaining_budget = budget - (initial_orange * orange_price) - (initial_mango * mango_price)

    # Calculate the amount of orange juice that can be added
    orange_to_add = min(remaining_capacity, remaining_budget / orange_price)

    # Update the remaining capacity and budget
    remaining_capacity -= orange_to_add
    remaining_budget -= orange_to_add * orange_price

    # Calculate the amount of mango juice that can be added
    mango_to_add = min(remaining_capacity, remaining_budget / mango_price)

    return orange_to_add, mango_to_add