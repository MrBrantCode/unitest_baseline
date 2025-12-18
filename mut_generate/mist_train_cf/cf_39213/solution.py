"""
QUESTION:
Create a function `calculateChange(totalPrice, amountPaid)` that calculates the change to be returned to a customer after a purchase. The function takes in two parameters: `totalPrice` (float) and `amountPaid` (float), both of which are positive floating-point numbers. The function should return the amount of change to be returned to the customer, or 0 if the amount paid is less than the total price.
"""

def entrance(totalPrice, amountPaid):
    if amountPaid < totalPrice:
        return 0
    else:
        return amountPaid - totalPrice