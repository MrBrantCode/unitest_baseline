"""
QUESTION:
Create a function `calculate_tip` that takes three arguments: the total bill `amount`, the `tip_percent`, and the preferred `currency`. The function should calculate the tip amount and total amount after tip in the specified currency, rounding the tip amount up to the nearest dollar and the total amount to the nearest cent. The function should accommodate various exchange rates, using the following exchange rates: USD (1.0), EUR (0.85), GBP (0.75), and any additional currencies as required.
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