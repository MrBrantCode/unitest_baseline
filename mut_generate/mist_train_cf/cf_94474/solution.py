"""
QUESTION:
Create a function called `check_price` that takes in a parameter `price` and returns a boolean value. The function should return `True` if the price is 10 or less and `False` otherwise. If the price is greater than 10, it should print the message 'Price must be 10 or less'.
"""

def check_price(price):
    if price > 10:
        print('Price must be 10 or less')
        return False
    else:
        return True