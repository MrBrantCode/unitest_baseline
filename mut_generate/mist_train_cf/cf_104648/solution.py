"""
QUESTION:
Write a function `get_fruits(items)` that takes a list of grocery items as input and returns a new list containing only the fruits from the input list. The function should be case-insensitive when identifying fruits, which are "apple", "banana", and "grapes".
"""

def get_fruits(items):
    fruits = []
    for item in items:
        if item.lower() in ["apple", "banana", "grapes"]:
            fruits.append(item)
    return fruits