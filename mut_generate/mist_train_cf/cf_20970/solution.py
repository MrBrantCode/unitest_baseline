"""
QUESTION:
Create a function `calculate_total_cost` that takes a list of dictionaries representing items in a shopping list, where each dictionary contains the keys 'name' and 'price'. Calculate the total cost of all items with a price less than or equal to $10, excluding items that exceed this price. Round the total cost to the nearest cent without using built-in rounding functions. Return the total cost as a string with the dollar sign symbol included. Additionally, print the number of items excluded due to their price exceeding $10.
"""

def calculate_total_cost(shopping_list):
    """
    Calculate the total cost of items in a shopping list with a price less than or equal to $10.

    Args:
        shopping_list (list): A list of dictionaries containing 'name' and 'price' of items.

    Returns:
        str: The total cost as a string with the dollar sign symbol included.
    """
    total_cost = 0
    num_excluded = 0
    
    for item in shopping_list:
        if item['price'] <= 10:
            total_cost += item['price']
        else:
            num_excluded += 1
    
    # Round the total cost to the nearest cent without using built-in rounding functions
    total_cost = int(total_cost * 100 + 0.5) / 100
    
    # Print the number of excluded items
    print("Number of excluded items: " + str(num_excluded))
    
    # Return the total cost as a string with the dollar sign symbol included
    return "$" + str(total_cost)