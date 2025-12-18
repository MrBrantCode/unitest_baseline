"""
QUESTION:
Create a function called `calculate_total_price` that takes a list of products and their corresponding prices, a list of products in the cart, and a discount (optional) as input. The function should return the total price of the products in the cart after applying the discount.

The function should accept the following parameters:
- `products`: A dictionary where the keys are product names and the values are prices.
- `cart`: A list of product names.
- `discount`: An optional parameter representing the discount percentage (default is 0).

The function should return the total price of the products in the cart after applying the discount.
"""

def calculate_total_price(products, cart, discount=0):
    """
    Calculate the total price of products in the cart after applying a discount.

    Args:
    - products (dict): A dictionary where keys are product names and values are prices.
    - cart (list): A list of product names.
    - discount (float, optional): The discount percentage. Defaults to 0.

    Returns:
    - float: The total price of the products in the cart after applying the discount.
    """
    # Calculate the total price of the products in the cart
    total_price = sum(products[product] for product in cart)

    # Calculate the discount amount
    discount_amount = (total_price / 100) * discount

    # Apply the discount to the total price
    total_price -= discount_amount

    return total_price