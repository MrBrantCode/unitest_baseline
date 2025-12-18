"""
QUESTION:
Write a function called calculate_total_cost that takes in a list of items and a dictionary of tax rates, along with a default tax rate. Each item in the list has attributes 'name', 'price', 'category', and 'weight'. The function should calculate the price of each item by multiplying its 'price' by its 'weight', apply the tax rate for the item's 'category' if it exists in the tax rates dictionary, or the default tax rate otherwise, and return the sum of the total cost for all items.
"""

def calculate_total_cost(items, tax_rates, default_tax_rate):
    """
    Calculate the total cost of a list of items after applying tax.

    Args:
        items (list): A list of dictionaries containing item information.
        tax_rates (dict): A dictionary of tax rates for different categories.
        default_tax_rate (float): The default tax rate to apply if a category is not found.

    Returns:
        float: The total cost of all items.
    """
    total_cost = 0
    for item in items:
        item_price = item["price"] * item["weight"]
        tax_rate = tax_rates.get(item["category"], default_tax_rate)
        total_price = item_price * (1 + tax_rate / 100)
        total_cost += total_price
    return total_cost