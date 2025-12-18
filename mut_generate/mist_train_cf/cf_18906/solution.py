"""
QUESTION:
Create a function named "calculate_total_price" that takes two parameters: "items" (a list of dictionaries) and "tax_rate" (a float representing the tax rate in decimal form). Each dictionary in the list represents an item with keys "name", "price", and "quantity". The function should return the total price of the items, including taxes, rounded to two decimal places. The total price is calculated by summing up the product of "price" and "quantity" for each item, adding the tax amount (total price multiplied by tax rate), and then rounding to two decimal places.
"""

def calculate_total_price(items, tax_rate):
    total_price = sum(item["price"] * item["quantity"] for item in items)
    total_price += total_price * tax_rate
    return round(total_price, 2)