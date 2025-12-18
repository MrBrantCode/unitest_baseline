"""
QUESTION:
Create a function called `calculate_average_price` that calculates the average price of a list of dictionaries, where each dictionary contains the keys 'name' and 'price'. The function should return the average price rounded to 2 decimal places.
"""

def calculate_average_price(list_of_dict):
    """
    Calculate the average price of a list of dictionaries.

    Args:
        list_of_dict (list): A list of dictionaries, each containing 'name' and 'price' keys.

    Returns:
        float: The average price rounded to 2 decimal places.
    """
    total_price = sum(item['price'] for item in list_of_dict)
    return round(total_price / len(list_of_dict), 2)