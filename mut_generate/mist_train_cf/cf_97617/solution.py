"""
QUESTION:
Write a function named `sort_ice_creams` that takes two inputs: a list of at least 7 tuples representing ice cream flavors, prices, and dietary information, and a list of dietary restrictions to exclude. The function should sort the list of ice cream flavors by price in ascending order, excluding flavors that contain any of the specified dietary restrictions, and return the sorted list. Each tuple in the input list should contain a string representing the ice cream flavor, a float representing the price, and a list of strings representing the dietary information.
"""

def sort_ice_creams(ice_creams, exclude_dietary):
    return sorted([ice_cream for ice_cream in ice_creams if not any(dietary in exclude_dietary for dietary in ice_cream[2])], key=lambda x: x[1])