"""
QUESTION:
Write a function `filter_products` that selects records from a database table `products` with a `price` less than 50, a `quantity` greater than 10, and a `name` starting with the letter "A".
"""

def filter_products(products):
    """
    Filters products based on price, quantity, and name.

    Args:
    products (list): A list of dictionaries, each containing product information.

    Returns:
    list: A list of dictionaries representing the filtered products.
    """
    return [product for product in products if product['price'] < 50 and product['quantity'] > 10 and product['name'].startswith('A')]