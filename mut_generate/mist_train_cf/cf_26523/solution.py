"""
QUESTION:
Implement a function `filter_items` that takes a list of dictionaries as input. Each dictionary represents an item and contains the keys 'name' (string), 'price' (float), and 'debug' (boolean). Filter the items based on the following criteria: include items with a price less than 100, and include items with a price greater than or equal to 100 only if the 'debug' key is set to True. Return a list of dictionaries that satisfy the filtering criteria.
"""

def filter_items(items):
    return [item for item in items if item['price'] < 100 or (item['price'] >= 100 and item['debug'])]