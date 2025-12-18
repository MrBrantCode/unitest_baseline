"""
QUESTION:
Create a function named "calculate_total_price" that takes two parameters: "items" (a list of dictionaries) and "tax_rate" (a float representing the tax rate in decimal form). Each dictionary in the list contains the keys "name", "price", and "quantity" representing the name, price, and quantity of an item respectively. The function should return the total price of the items including taxes, rounded to two decimal places.
"""

def calculate_total_price(items, tax_rate):
    """
    Calculate the total price of items including taxes.

    Args:
        items (list): A list of dictionaries containing item information.
        tax_rate (float): The tax rate in decimal form.

    Returns:
        float: The total price of items including taxes, rounded to two decimal places.
    """
    total_price = sum(item["price"] * item["quantity"] for item in items)
    tax_amount = total_price * tax_rate
    return round(total_price + tax_amount, 2)