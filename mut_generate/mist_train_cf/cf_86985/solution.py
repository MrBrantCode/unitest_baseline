"""
QUESTION:
Create a function named `convert_currency` that takes in a currency amount and an exchange rate dictionary, and returns the converted amounts for one or more currencies. The exchange rate dictionary should have currency codes as keys and exchange rates as values. The function should handle decimal places in the input amount.
"""

def convert_currency(amount, exchange_rate, *currencies):
    converted_amounts = []
    for currency in currencies:
        converted_amount = amount * exchange_rate[currency]
        converted_amounts.append(converted_amount)
    
    return converted_amounts