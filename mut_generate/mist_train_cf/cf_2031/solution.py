"""
QUESTION:
Write a function called "check_price" that takes in a parameter called "price" and returns a boolean value indicating whether the price is a prime number. If the price is not a prime number, print the message 'Price must be a prime number' and return False. Note that prime numbers are numbers greater than 1 that have no divisors other than 1 and themselves.
"""

def check_price(price):
    if price < 2:
        print('Price must be a prime number')
        return False
    for i in range(2, int(price ** 0.5) + 1):
        if price % i == 0:
            print('Price must be a prime number')
            return False
    return True