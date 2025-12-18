"""
QUESTION:
Write a function called `check_price` that takes a `price` as a parameter. The function should return `True` if the `price` is 10 or less, and `False` otherwise. If the `price` is greater than 10, print the message 'Price must be 10 or less'.
"""

def check_price(price):
    if price > 10:
        print('Price must be 10 or less')
        return False
    else:
        return True