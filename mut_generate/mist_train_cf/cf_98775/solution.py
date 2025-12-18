"""
QUESTION:
Write a function `highest_price` that takes a table of products and their prices as input, where each product is represented by a tuple of the product name and its price. The function should return a list of the product names with the highest price. If there are multiple products with the same highest price, all of them should be included in the output list.
"""

def highest_price(table):
    highest_price = 0
    corresponding_products = []
    for row in table:
        product, price = row
        if price > highest_price:
            highest_price = price
            corresponding_products = [product]
        elif price == highest_price:
            corresponding_products.append(product)
    return corresponding_products