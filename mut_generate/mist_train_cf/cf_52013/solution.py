"""
QUESTION:
Create a function `fruit_distribution(s, n, fruits, fruit_prices)` that takes a string array `s` containing the amount of various fruits in a consignment, an integer `n` representing the total price tag attached to all diverse fruits within the consignment, a list of strings `fruits` containing all distinct fruit types, and a dictionary `fruit_prices` associating every distinct fruit type with its respective market price.

The function should return a dictionary that denotes the quantity of any unmentioned fruit in the array, deriving said quantity from the market price of the fruit and the composite consignment cost. The final output should only include fruit types with a populated count (i.e., a count exceeding zero).
"""

def fruit_distribution(s, n, fruits, fruit_prices):
    distribution = {}
    for fruit in fruits:
        distribution[fruit] = 0
    for record in s:
        record = record.split(' ')
        quantity = int(record[0])
        fruit = record[1]
        distribution[fruit] += quantity
        n -= quantity * fruit_prices[fruit]
    for fruit in fruits:
        if distribution[fruit] == 0:
            distribution[fruit] = n // fruit_prices[fruit]
            n -= distribution[fruit] * fruit_prices[fruit]
    return {k: v for k, v in distribution.items() if v > 0}