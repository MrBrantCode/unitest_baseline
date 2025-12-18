"""
QUESTION:
Create a function `calculate_tip` that takes in the total bill `amount`, the desired `tip_percent`, and the user's preferred `currency` as parameters. The function should return a tuple containing the tip amount and the total amount after tip, both rounded accordingly. The tip amount should be rounded up to the nearest dollar, while the total amount should be rounded to the nearest cent. The function should also accommodate various exchange rates for different currencies.
"""

import math

EXCHANGE_RATES = {
 'USD': 1.0,
 'EUR': 0.85,
 'GBP': 0.75,
 # add more currencies and exchange rates here
}

def calculate_tip(amount, tip_percent, currency):
    exchange_rate = EXCHANGE_RATES[currency]
    tip_amount = math.ceil(amount * tip_percent / 100)
    total_amount = round((amount + tip_amount) * exchange_rate, 2)
    return (tip_amount, total_amount)