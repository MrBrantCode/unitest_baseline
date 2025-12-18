"""
QUESTION:
Create a function named `calculate_original_price` that takes a list of items, where each item is a tuple containing the item name, current price, and discount percentage. The function should calculate the original price of each item, the amount discounted, and return the results as a list of tuples containing the item name, original price, and amount discounted. The results should be sorted in descending order by the amount discounted, and all prices should be rounded to 2 decimal places.
"""

import operator

def calculate_original_price(items):
    """
    Calculate the original price of each item, the amount discounted, 
    and return the results as a list of tuples containing the item name, 
    original price, and amount discounted.

    Args:
    items (list): A list of items, where each item is a tuple containing 
                  the item name, current price, and discount percentage.

    Returns:
    list: A list of tuples containing the item name, original price, 
          and amount discounted, sorted in descending order by the amount discounted.
    """
    calculation_results = []
    for item in items:
        current_price = item[1]
        discount_percentage = item[2]
        original_price = round(current_price / ((100 - discount_percentage) / 100), 2)
        amount_discounted = round(original_price - current_price, 2)
        calculation_results.append((item[0], original_price, amount_discounted))

    # Sort in descending order by the amount discounted
    calculation_results.sort(key=operator.itemgetter(2), reverse=True)

    return calculation_results