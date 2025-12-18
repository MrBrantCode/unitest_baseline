"""
QUESTION:
Create a function `price_tag` that takes in the following parameters: a cost, city tax rate, state tax rate, federal tax rate, and a list of discounts. The function should calculate the initial price by applying the cumulative tax rate to the cost, then calculate the final price by applying each discount in the list successively to the initial price. The function should also calculate the total tax amount on the cost. Return the initial price, final price, and total tax amount as strings, rounded to two decimal places.
"""

def price_tag(cost, city_tax, state_tax, federal_tax, discounts):
    # Calculate total tax rate
    total_tax_rate = city_tax + state_tax + federal_tax

    # Apply tax to cost
    initial_price = cost * (1 + total_tax_rate)
    final_price = initial_price

    # Apply discounts
    for discount in discounts:
        final_price *= (1 - discount)

    return "{:.2f}".format(initial_price), "{:.2f}".format(final_price), "{:.2f}".format(total_tax_rate * cost)