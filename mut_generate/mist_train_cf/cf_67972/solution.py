"""
QUESTION:
Calculate the total expenditure for a given quantity of products, taking into account a dynamic discount rate and a tax rate. The discount rate decreases the unit price by 0.1% for every 100 items purchased. The function should be able to handle large quantities.

Develop a function named `calculate_total_expenditure(quantity, unit_price, tax_rate)` that calculates the total expenditure based on these factors. The function should return the total expenditure, including tax. Assume the tax rate is a percentage.
"""

def calculate_total_expenditure(quantity, unit_price, tax_rate):
    total = 0
    for i in range(quantity):
        if i % 100 == 0 and i != 0:
            unit_price *= 0.999  # decrease price by 0.1% for each 100 items
        total += unit_price

    tax = total * tax_rate / 100
    return total + tax