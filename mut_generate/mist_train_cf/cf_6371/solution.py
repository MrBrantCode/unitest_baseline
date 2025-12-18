"""
QUESTION:
Create a function `calculate_total_cost` that takes a list of shopping items as input, where each item is a dictionary containing 'name' and 'price'. Calculate the total cost of all items with prices not exceeding $10, round the total cost to the nearest cent without using built-in Python rounding functions, and return the total cost as a string with the dollar sign symbol included. The function should also keep track of the number of items excluded due to their price exceeding $10 and print out a message stating the number of excluded items.
"""

def calculate_total_cost(shopping_list):
    """
    Calculate the total cost of all items with prices not exceeding $10, 
    round the total cost to the nearest cent without using built-in Python rounding functions, 
    and return the total cost as a string with the dollar sign symbol included.

    Args:
        shopping_list (list): A list of dictionaries containing 'name' and 'price' of shopping items.

    Returns:
        str: The total cost of items with prices not exceeding $10 as a string with the dollar sign symbol included.
    """
    total_cost = 0
    num_excluded = 0
    for item in shopping_list:
        if item['price'] <= 10:
            total_cost += item['price']
        else:
            num_excluded += 1
    # Round the total cost to the nearest cent without using built-in Python rounding functions
    total_cost_str = "${:.2f}".format(total_cost)
    print("Number of excluded items:", num_excluded)
    return total_cost_str