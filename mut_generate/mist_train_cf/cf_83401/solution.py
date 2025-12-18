"""
QUESTION:
Develop a function named `total_cost` that calculates the total cost of purchasing a certain number of products. The function should take the following parameters: `no_of_products` (the number of products being purchased), `unit_cost` (the cost of a single product), and optional parameters `bulk_threshold` (the minimum number of products required for a bulk discount) and `discount_rate` (the percentage discount applied for bulk purchases). If `bulk_threshold` and `discount_rate` are provided and `no_of_products` meets or exceeds `bulk_threshold`, apply the discount to the total cost. Otherwise, calculate the total cost as the product of `no_of_products` and `unit_cost`.
"""

def total_cost(no_of_products, unit_cost, bulk_threshold=None, discount_rate=None):
    if bulk_threshold and no_of_products >= bulk_threshold and discount_rate:
        cost = no_of_products * unit_cost * (1 - discount_rate/100)
    else:
        cost = no_of_products * unit_cost

    return cost