"""
QUESTION:
Write a function `calculate_total_price` that takes two dictionaries, `table1` and `table2`, and a string `ingredient` as input. Each dictionary represents a table with menu entries where keys are unique identifiers and values are dictionaries containing the dish name, price, and a list of ingredients. The function should return the total price of all dishes from both tables that include the specified `ingredient`.
"""

def calculate_total_price(table1, table2, ingredient):
    total_price = 0
    
    for food in table1.values():
        if ingredient in food["ingredients"]:
            total_price += food["price"]
    
    for food in table2.values():
        if ingredient in food["ingredients"]:
            total_price += food["price"]
    
    return total_price