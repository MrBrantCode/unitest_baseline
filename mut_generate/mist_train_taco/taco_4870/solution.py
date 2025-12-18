"""
QUESTION:
problem

At the JOI pasta shop, the recommended pasta for lunch and the set menu of freshly squeezed juice are popular. When ordering this set menu, choose one from each of the three pasta and two juices of the day. The price is the total price of pasta and juice minus 50 yen.

Given the price of pasta and juice for a day, create a program to find the minimum price for the set menu for that day.



output

Output the minimum price of the set menu for the day in one line.

Example

Input

800
700
900
198
330


Output

848
"""

def calculate_minimum_set_menu_price(pasta_prices, juice_prices):
    # Calculate the minimum price of pasta and juice
    min_pasta_price = min(pasta_prices)
    min_juice_price = min(juice_prices)
    
    # Calculate the total minimum price of the set menu
    total_minimum_price = min_pasta_price + min_juice_price - 50
    
    return total_minimum_price