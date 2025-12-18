"""
QUESTION:
Create a function `organize_by_key` that takes two parameters: `values` (a list of dictionaries) and `key` (a string representing the key to sort by). The function should return a list of dictionaries sorted in ascending order by the values of the specified key. The function should allow for optional sorting in descending order.
"""

def organize_by_key(values, key, reverse=False):
    return sorted(values, key = lambda x: x[key], reverse=reverse)