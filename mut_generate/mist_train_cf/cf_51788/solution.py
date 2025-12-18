"""
QUESTION:
Write a function `calculate_change` that determines the number of quarters, half-dollars, and dollar bills needed to reach a specific total amount. The function should take an integer `total_amount` as input and return a tuple containing the number of quarters, half-dollars, and dollar bills required. Assume that the available coins and bills have fixed values of $0.25, $0.50, and $1.00 respectively.
"""

def calculate_change(total_amount):
    """
    Calculate the number of quarters, half-dollars, and dollar bills needed to reach a specific total amount.

    Args:
        total_amount (int): The total amount to be reached.

    Returns:
        tuple: A tuple containing the number of quarters, half-dollars, and dollar bills required.
    """
    total_amount_cents = total_amount * 100  # Convert dollars to cents
    dollar_bills = total_amount_cents // 100
    remaining_amount = total_amount_cents % 100
    half_dollars = remaining_amount // 50
    remaining_amount %= 50
    quarters = remaining_amount // 25
    return quarters, half_dollars, dollar_bills