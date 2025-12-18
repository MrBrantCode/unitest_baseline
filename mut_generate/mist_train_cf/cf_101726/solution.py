"""
QUESTION:
Write a function named `calculate_tip` that calculates the tip amount and total amount after rounding the tip to the nearest dollar and the total to the nearest cent. The function should take three parameters: `amount` (the initial bill amount), `tip_percent` (the tip percentage), and `currency` (the currency code). The function should use a predefined dictionary of exchange rates (`EXCHANGE_RATES`) to convert the amounts to the specified currency.
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