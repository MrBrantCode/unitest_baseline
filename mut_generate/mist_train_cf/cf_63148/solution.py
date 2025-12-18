"""
QUESTION:
Create a function `calculate_net_price` that calculates the net price of a product given its base cost, applied discount percentage, and country of sale. The function should apply the corresponding tax rate based on the country, handle fractional penny rounding, and return the net price. Assume tax rates for different countries are provided as a dictionary. The function should take three parameters: `cost`, `discount`, and `country`.
"""

def calculate_net_price(cost, discount, country):
    tax_rates = {'USA': 5.6, 'UK': 20, 'Germany': 19, 'China': 13}   # assuming these tax rates
    tax_rate = tax_rates[country]
    
    # Calculate discount price
    discounted_price = cost * (1 - (discount/100))
    
    # Apply tax
    price_with_tax = discounted_price * (1 + (tax_rate/100))

    # Round to nearest penny (0.01)
    net_price = round(price_with_tax, 2)
    return net_price