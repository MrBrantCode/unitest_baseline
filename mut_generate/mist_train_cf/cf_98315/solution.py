"""
QUESTION:
Create a function named `calculate_tip` that takes in three arguments: the bill amount, the tip percentage, and the currency code. The function should return a tuple containing the tip amount and the total amount. The tip amount should be rounded up to the nearest dollar and the total amount should be rounded to the nearest cent. The function should also be able to accommodate various exchange rates, which can be stored in a dictionary where the keys are the currency codes and the values are the corresponding exchange rates.
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
    total_amount = math.ceil((amount + tip_amount) * exchange_rate * 100) / 100
    return (tip_amount, total_amount)