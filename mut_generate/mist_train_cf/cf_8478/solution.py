"""
QUESTION:
Write a function sum_quantities(blocks) that takes in a list of dictionaries representing blocks. Each dictionary contains 'order_id', 'quantity', and 'price' keys. Return the sum of the quantities for blocks where quantity is at least 5 and price is less than 200, assuming all quantities and prices are positive integers.
"""

def sum_quantities(blocks):
    total_quantity = 0
    for block in blocks:
        if block['quantity'] >= 5 and block['price'] < 200:
            total_quantity += block['quantity']
    return total_quantity