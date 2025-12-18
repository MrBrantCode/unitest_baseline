"""
QUESTION:
Write a Python function named `calculate_total_bill` that computes the total amount of a given grocery bill after taxes and discounts. The function should take three arguments: 
- a list of tuples where each tuple represents an item and its price, 
- a float representing the tax rate as a decimal, 
- and a dictionary representing any applicable discounts or promotions where the keys are the item names and the values are the respective discounts as decimals.

The function should return a tuple containing two values: 
- a float representing the total amount of the grocery bill after taxes and discounts, 
- a list of tuples where each tuple represents an item purchased and its final price after taxes and discounts.

The function should handle cases where an item is not in the discounts dictionary.
"""

def calculate_total_bill(items, tax_rate, discounts):
    total_amount = 0
    itemized_list = []

    for item, price in items:
        if item in discounts:
            discounted_price = price - (price * discounts[item])
        else:
            discounted_price = price

        taxed_price = discounted_price + (discounted_price * tax_rate)

        total_amount += taxed_price
        itemized_list.append((item, taxed_price))

    return total_amount, itemized_list