"""
QUESTION:
Create a function named `convert_currency` that takes two parameters: `amount` and `exchange_rate`. The function should return the converted amount after multiplying the input `amount` by the `exchange_rate`, rounded to 2 decimal places.
"""

def convert_currency(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return round(converted_amount, 2)  # Round to 2 decimal places