"""
QUESTION:
Implement a function `find_most_expensive_product(table)` that takes in a list of tuples `table`, where each tuple contains a product name (string) and its corresponding price (float). The function should return the name of the product with the highest price in the table. Assume the table is non-empty and all prices are non-negative.
"""

def find_most_expensive_product(table):
    max_price = float('-inf')
    max_product = None
    for product, price in table:
        if price > max_price:
            max_price = price
            max_product = product
    return max_product