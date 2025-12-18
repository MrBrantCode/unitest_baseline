"""
QUESTION:
Write a function `calculate_price_sum` that takes a list of dictionaries as input, where each dictionary can contain multiple keys starting with "price" followed by an optional integer suffix (e.g., "price", "price_1", "price_2", etc.), and returns the aggregated sum of all price values across the list as an integer. Ensure the function handles cases where some dictionaries may not have a price key and optimize for performance with large lists.
"""

def calculate_price_sum(list_of_dicts):
    total = 0
    for dictionary in list_of_dicts:
        for key, value in dictionary.items():
            if key.startswith('price'):
                total += value
    return total