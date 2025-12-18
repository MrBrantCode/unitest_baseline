"""
QUESTION:
The pizza store wants to know how long each order will take. They know:

- Prepping a pizza takes 3 mins
- Cook a pizza takes 10 mins
- Every salad takes 3 mins to make
- Every appetizer takes 5 mins to make
- There are 2 pizza ovens
- 5 pizzas can fit in a oven
- Prepping for a pizza must be done before it can be put in the oven
- There are two pizza chefs and one chef for appitizers and salads combined
- The two pizza chefs can work on the same pizza

Write a function, order, which will tell the company how much time the order will take.

See example tests for details.
"""

from math import ceil

def calculate_order_time(pizzas, salads, appetizers):
    # Time to prep and cook pizzas
    pizza_prep_time = 3 * pizzas / 2  # Since there are 2 pizza chefs
    pizza_cook_time = 10 * ceil(pizzas / 5)  # Since 5 pizzas can fit in an oven
    total_pizza_time = pizza_prep_time + pizza_cook_time
    
    # Time to make salads and appetizers
    total_salad_time = 3 * salads
    total_appetizer_time = 5 * appetizers
    total_salad_appetizer_time = total_salad_time + total_appetizer_time
    
    # The total order time is the maximum of the pizza time and the salad/appetizer time
    total_order_time = max(total_pizza_time, total_salad_appetizer_time)
    
    return total_order_time