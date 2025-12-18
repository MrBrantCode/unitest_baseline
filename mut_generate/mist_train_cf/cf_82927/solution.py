"""
QUESTION:
Write a function `calculate_phone_prices` that takes as input four variables: 
- `total_revenue` (t): the total revenue generated from both phone models, 
- `total_phones_sold` (b + r): the total number of phones sold, 
- `difference_in_phones_sold` (d): the difference in the number of budget and premium phones sold, and 
- `price_difference_percentage` (x): the percentage of price difference between the premium and budget models in decimal form.

The function should return the prices of the budget phone (p) and the premium phone (P).
"""

def calculate_phone_prices(total_revenue, total_phones_sold, difference_in_phones_sold, price_difference_percentage):
    """
    This function calculates the prices of the budget phone (p) and the premium phone (P).
    
    Parameters:
    total_revenue (float): The total revenue generated from both phone models.
    total_phones_sold (int): The total number of phones sold.
    difference_in_phones_sold (int): The difference in the number of budget and premium phones sold.
    price_difference_percentage (float): The percentage of price difference between the premium and budget models in decimal form.

    Returns:
    tuple: A tuple containing the price of the budget phone (p) and the price of the premium phone (P).
    """

    # Calculate the number of premium phones sold
    premium_phones_sold = (total_phones_sold - difference_in_phones_sold) / 2
    
    # Calculate the price of the budget phone
    budget_phone_price = total_revenue / ((1 + price_difference_percentage) * premium_phones_sold + difference_in_phones_sold)
    
    # Calculate the price of the premium phone
    premium_phone_price = (1 + price_difference_percentage) * budget_phone_price
    
    return budget_phone_price, premium_phone_price