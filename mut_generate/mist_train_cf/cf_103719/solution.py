"""
QUESTION:
Write a function `calculate_total_price` that takes a dictionary where each value is another dictionary with 'price' and 'quantity' keys. The function should return the total price of all items by multiplying 'price' and 'quantity', ignoring any 'quantity' that is not a number.
"""

def calculate_total_price(dictionary):
    """
    Calculate the total price of all items in a dictionary.

    Args:
        dictionary (dict): A dictionary where each value is another dictionary with 'price' and 'quantity' keys.

    Returns:
        float: The total price of all items.
    """
    total_price = 0
    for item in dictionary.values():
        try:
            price = item['price']
            quantity = item['quantity']
            if isinstance(quantity, (int, float)):  # Check if quantity is a number
                total_price += price * quantity
        except KeyError:
            continue
    return total_price