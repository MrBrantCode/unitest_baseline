"""
QUESTION:
The function `calculate_tip(amount, tip_percent, currency)` should take the bill amount, tip percentage, and currency as input and return the tip amount and total amount. The function should accommodate various exchange rates and round the tip amount up to the nearest dollar and the total amount to the nearest cent. The function should use a dictionary or an API to fetch the exchange rates for different currencies. The function should not take any other parameters other than the three specified.
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
    tip_amount = math.ceil(amount * tip_percent / 100 / exchange_rate)
    total_amount = math.ceil((amount / exchange_rate + tip_amount) * 100) / 100
    return (tip_amount, total_amount)