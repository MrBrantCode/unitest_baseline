"""
QUESTION:
Write a function `min_coins(amount)` that determines the least quantity of coins necessary to accurately represent a specified monetary sum using the standard US coin denominations (25, 10, 5, 1).
"""

def min_coins(amount):
    denominations = [25, 10, 5, 1]
    coins_used = 0
    for denom in denominations:
        while amount >= denom:
            amount -= denom
            coins_used += 1
    return coins_used