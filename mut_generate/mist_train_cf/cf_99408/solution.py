"""
QUESTION:
Write a function `calculate_tip` that takes in three parameters: `amount`, `tip_percent`, and `currency`. The function should return a tuple containing the tip amount and the total amount, where the tip amount is rounded up to the nearest dollar and the total amount is rounded to the nearest cent. The function should also accommodate different currencies based on their exchange rates with the USD. The exchange rates should be stored in a dictionary, where the keys are the currency codes and the values are the corresponding exchange rates.
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