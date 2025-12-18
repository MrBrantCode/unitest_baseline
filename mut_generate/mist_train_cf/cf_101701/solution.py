"""
QUESTION:
Write a function named `sort_ice_creams` that takes two parameters: `ice_creams` and `exclude_dietary`. `ice_creams` is a list of at least 7 tuples, where each tuple contains a string representing an ice cream flavor, a float representing its price, and a list of strings representing its dietary information. `exclude_dietary` is a list of strings representing dietary restrictions to exclude from the list of available flavors. The function should sort the ice cream flavors by increasing price, excluding any flavors with certain dietary restrictions, and return the sorted list of available flavors and their prices along with their corresponding dietary information.
"""

def sort_ice_creams(ice_creams, exclude_dietary):
    return sorted([ice_cream for ice_cream in ice_creams if not any(dietary in exclude_dietary for dietary in ice_cream[2])], key=lambda x: x[1])