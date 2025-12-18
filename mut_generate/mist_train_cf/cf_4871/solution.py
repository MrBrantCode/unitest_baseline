"""
QUESTION:
Write a function named `calculate_total_price` that takes a list of products as input, where each product is a tuple of price, quantity, and weight. Calculate the total price by summing the product of price and quantity for each product with a weight of 10 units or less, then divide the result by the total weight of these products. If no products meet the weight criteria, return 0.
"""

def calculate_total_price(products):
    """
    Calculate the total price by summing the product of price and quantity 
    for each product with a weight of 10 units or less, then divide the result 
    by the total weight of these products.

    Args:
        products (list): A list of products, where each product is a tuple of price, quantity, and weight.

    Returns:
        float: The total price of the products meeting the weight criteria.
    """
    total_price = sum(price * quantity for price, quantity, weight in products if weight <= 10)
    total_weight = sum(weight for _, _, weight in products if weight <= 10)
    
    return total_price / total_weight if total_weight != 0 else 0