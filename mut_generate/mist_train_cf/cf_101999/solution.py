"""
QUESTION:
Write a function `get_average_and_count` that takes a list of dictionaries `data` as input, where each dictionary represents an item with a 'price' key. The function should return a tuple containing the average price and the count of items whose price is greater than or equal to 5 and less than or equal to 10, rounded to the nearest whole number. If no items satisfy the condition or the input list is empty, the function should return (0, 0).
"""

import math

def get_average_and_count(data):
    if len(data) == 0:
        return 0, 0

    total = 0
    count = 0

    for item in data:
        price = item['price']
        if price >= 5 and price <= 10:
            total += price
            count += 1

    if count == 0:
        return 0, 0

    average = round(total / count)
    return average, count