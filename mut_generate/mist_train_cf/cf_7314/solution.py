"""
QUESTION:
Write a function to find the product with the maximum price in a database, excluding products priced over $1000 and not sold in the last 6 months. The function should return the name and category of the product with the maximum price.
"""

from datetime import datetime, timedelta

def max_priced_product(products):
    """
    Find the product with the maximum price in a database, excluding products priced over $1000 and not sold in the last 6 months.

    Args:
        products (list): A list of dictionaries containing product information (name, category, price, last_sold).

    Returns:
        tuple: The name and category of the product with the maximum price.
    """
    six_months_ago = datetime.now() - timedelta(days=183)
    eligible_products = [product for product in products if product['price'] <= 1000 and product['last_sold'] >= six_months_ago]
    if not eligible_products:
        return None
    max_priced_product = max(eligible_products, key=lambda x: x['price'])
    return max_priced_product['name'], max_priced_product['category']