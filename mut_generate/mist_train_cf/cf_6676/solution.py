"""
QUESTION:
Write a function named `calculate_total_price` that takes in two dictionaries (`table1` and `table2`) and a string (`ingredient`) as input. Each dictionary represents a table and contains menu entries as its values, with each menu entry having a 'price' and a list of 'ingredients'. The function should return the total price of all the dishes from both tables that contain the specified ingredient.
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