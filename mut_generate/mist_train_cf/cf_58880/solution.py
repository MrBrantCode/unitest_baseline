"""
QUESTION:
Construct a display table for food orders in a restaurant. The function `displayTable` should take a list `orders` of customer orders as input, where each order is a list containing the customer's name, table number, and food item. The function should return a 2D list representing the display table, where each row indicates the quantity of each food item ordered by each table.

The function should follow these restrictions:
- The first column represents the table number.
- The subsequent columns correspond to each food item, arranged in alphabetical order.
- The first row is a header row with the first column labeled as "Table", followed by the names of the food items.
- The rows should be sorted in ascending numerical order.
- The function should be able to handle up to 5 * 10^4 orders.
- Each order should contain a valid integer table number between 1 and 500, and the customer name and food item should consist of lowercase and uppercase English letters and the space character.
"""

from collections import Counter

def displayTable(orders):
    foods = set()
    tables = {}
    for name, table, food in orders:
        foods.add(food)
        if table not in tables:
            tables[table] = Counter()
        tables[table][food] += 1
    foods = sorted(foods)
    table_numbers = sorted(tables, key=int)
    results = [["Table"] + foods]
    for table in table_numbers:
        results.append([table] + [str(tables[table][food]) for food in foods])
    return results