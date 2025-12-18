"""
QUESTION:
Create a function `calculate_change_coins` that takes an integer `change` representing the amount of change in cents as input. The function should return the minimum number of quarters, dimes, nickels, and pennies required to make that change, following the rules of using the fewest number of coins possible and only using quarters, dimes, nickels, and pennies.
"""

def calculate_change_coins(change):
    quarters = change // 25
    change %= 25
    dimes = change // 10
    change %= 10
    nickels = change // 5
    pennies = change % 5
    return quarters, dimes, nickels, pennies