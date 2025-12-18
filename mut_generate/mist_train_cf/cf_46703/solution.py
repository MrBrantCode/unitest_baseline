"""
QUESTION:
Develop a function `compute_total_price` that calculates the total price of a given number of products with a variable sales tax rate. The sales tax rate starts at 7% and increases by 0.5% for every 5 additional products. The function should take the number of products as a required argument and the base tax rate, threshold number of products for tax increase, and tax increase rate as optional arguments with default values of 0.07, 5, and 0.005, respectively.
"""

def compute_total_price(num_products, base_tax_rate=0.07, threshold=5, increment_rate=0.005):
    """
    Calculate the total price of a given number of products with a variable sales tax rate.

    Args:
        num_products (int): The number of products.
        base_tax_rate (float, optional): The base tax rate. Defaults to 0.07.
        threshold (int, optional): The threshold number of products for tax increase. Defaults to 5.
        increment_rate (float, optional): The tax increase rate. Defaults to 0.005.

    Returns:
        float: The total price of the products.
    """
    total_tax_rate = base_tax_rate + (num_products // threshold) * increment_rate
    total_price = num_products * (1 + total_tax_rate)
    return total_price