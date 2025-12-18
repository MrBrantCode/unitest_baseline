"""
QUESTION:
Write a function `find_cheapest_product` that takes a list of products in JSON format and returns the product with the lowest cost among those that are in stock and whose name starts with a vowel. If there are multiple products with the same lowest cost, return the one with the highest cost. If no products meet the criteria, return a message indicating so.

The input list of products is a list of dictionaries where each dictionary contains the keys 'name', 'cost', and 'in_stock'. The 'in_stock' key has a boolean value and 'name' and 'cost' have string and integer values respectively. The function should return the product dictionary if a product meets the criteria or a message if no product meets the criteria.
"""

def find_cheapest_product(products):
    """
    This function finds the cheapest product in stock whose name starts with a vowel.
    If multiple products have the same lowest cost, it returns the one with the highest cost.
    If no products meet the criteria, it returns a message indicating so.

    Args:
        products (list): A list of dictionaries containing product information.
                         Each dictionary should have 'name', 'cost', and 'in_stock' keys.

    Returns:
        dict or str: The cheapest product dictionary if a product meets the criteria, otherwise a message.
    """

    # Initialize cheapest_cost to infinity and cheapest_product to None
    cheapest_cost = float('inf')
    cheapest_product = None

    # Iterate over each product in the list
    for product in products:
        # Check if the product is in stock
        if product['in_stock']:
            # Check if the product's name starts with a vowel
            if product['name'][0].lower() in ['a', 'e', 'i', 'o', 'u']:
                # Check if the product's cost is less than the current cheapest cost
                if product['cost'] < cheapest_cost:
                    # Update cheapest_cost and cheapest_product
                    cheapest_cost = product['cost']
                    cheapest_product = product
                # Check if the product's cost is equal to the current cheapest cost
                # and the product's cost is higher than the current cheapest product's cost
                elif product['cost'] == cheapest_cost and product['cost'] > cheapest_product['cost']:
                    # Update cheapest_product
                    cheapest_product = product

    # If no products meet the criteria, return a message
    if cheapest_product is None:
        return "No products meet the criteria."
    # Otherwise, return the cheapest product
    else:
        return cheapest_product