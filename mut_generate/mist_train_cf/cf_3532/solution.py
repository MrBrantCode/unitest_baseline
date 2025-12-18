"""
QUESTION:
Write a function named `average_price` that calculates the average price of products. The function should take a list of products as input where each product is a dictionary with 'category', 'price', 'in_stock', and 'brand' keys. It should return the average price of products in the "Electronics" category that have a price greater than $100, are out of stock ('in_stock' is False), and have a brand name starting with the letter "S".
"""

def average_price(products):
    """
    Calculate the average price of products in the "Electronics" category 
    that have a price greater than $100, are out of stock, and have a brand 
    name starting with the letter "S".

    Args:
        products (list): A list of products where each product is a dictionary 
                         with 'category', 'price', 'in_stock', and 'brand' keys.

    Returns:
        float: The average price of the filtered products.
    """

    # Filter products based on the category, price, stock status, and brand
    filtered_products = [
        product for product in products 
        if product['category'] == 'Electronics' 
        and product['price'] > 100 
        and not product['in_stock'] 
        and product['brand'].startswith('S')
    ]

    # Check if there are any filtered products
    if not filtered_products:
        return 0  # or any other default value that makes sense for your application

    # Calculate the average price of the filtered products
    average = sum(product['price'] for product in filtered_products) / len(filtered_products)

    return average