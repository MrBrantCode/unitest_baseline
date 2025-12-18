"""
QUESTION:
Write a function `get_fruits` that takes a list of grocery items as input and returns a new list containing only the fruits. The function should be case-insensitive when identifying fruits. The list of fruits to consider includes "apple", "banana", and "grapes".
"""

def get_fruits(grocery_items):
    fruits = []
    fruit_names = ["apple", "banana", "grapes"]
    for item in grocery_items:
        if item.lower() in fruit_names:
            fruits.append(item)
    return fruits