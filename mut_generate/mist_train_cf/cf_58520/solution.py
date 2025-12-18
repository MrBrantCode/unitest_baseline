"""
QUESTION:
Construct a function `unique_fruits` that takes a list of fruit names and a dictionary of fruit names with their quantities as input, and returns a list of unique fruit names in the original order, with each name capitalized. The function should have a time complexity of O(n), where n is the number of elements in the list of fruit names.
"""

def unique_fruits(fruit_list, fruit_dict):
    unique_fruits = []
    for fruit in fruit_list:
        if fruit not in unique_fruits:
            unique_fruits.append(fruit)
    return [fruit.capitalize() for fruit in unique_fruits]